from flask import Flask, render_template, request, abort, redirect, url_for
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)


def bootstrap_database():

    # This will create the database file using SQLAlchemy
    db.create_all()

    first_names = ['Donald', 'Marco', 'Jeb', 'Ben', 'Hillary', 'Bernie']
    last_names = ['Carson', 'Rubio', 'Trump', 'Bush', 'Sanders', 'Clinton']

    for fn in first_names:
        for ln in last_names:
            candidate = Contact()
            candidate.name = "{} {}".format(fn, ln)
            db.session.add(candidate)

    db.session.commit()


class Contact(db.Model):

    __tablename__ = 'contact'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128),  nullable=False)
    addresses = db.relationship(
        'Address', backref='contact',
        foreign_keys='Address.contact_id', lazy='dynamic'
    )

    def serialize(self):
        ret = {
            'id': self.id,
            'name': self.name,
            'addresses': [
                address.serialize()
                for address in self.addresses
            ]
        }
        return ret

#####################################################################
# STEP 1 -- define an Address model that relates to the Contact model
#####################################################################


class Address(db.Model):

    __tablename__ = 'address'
    id = db.Column(db.Integer, primary_key=True)
    contact_id = db.Column(db.Integer, db.ForeignKey('contact.id'))
    city = db.Column(db.String(128))
    street = db.Column(db.String(128))
    state = db.Column(db.String(128))
    zip_code = db.Column(db.String(128))
    address_type = db.Column(db.Enum(
        'home', 'work', name='address_types')
    )

    def serialize(self):
        ret = {
            'id': self.id,
            'city': self.city,
            'state': self.state,
            'street': self.street,
            'zip': self.zip_code,
            'type': self.address_type
        }
        return ret

    @staticmethod
    def is_valid_type(address_type):
        if address_type.lower() not in ('home', 'work'):
            return False
        return True

    @staticmethod
    def is_valid_form(*args):
        for arg in args:
            if len(arg) > 128:
                return False
        return True


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/search')
def search():
    #############################################################
    # STEP 2 -- use SQL Alchemy to query contacts based on having
    # names that contain or are equal to the query. If query is
    # "ar" it should find both "Marco Rubio" and "Ben Carson" (and
    # every other contact with either "Marco" or "Carson" in their
    # name)
    # You will also need to build the search.html view template.
    #############################################################
    search_query = request.args['query']
    contacts = Contact.query.\
        filter(Contact.name.contains(search_query)).all()

    contacts_list = [contact.serialize() for contact in contacts]

    return render_template('search.html', data=contacts_list)


@app.route('/contacts/<id>')
def show_contact(id):
    #############################################################
    # STEP 3 -- load a user and addresses based on the user's id
    # You will also need to build the show_contact.html view template.
    #############################################################
    error = None
    contact = Contact.query.filter_by(id=id).first()
    data = {}
    if not contact:
        error = "Contact not found"
    else:
        data = contact.serialize()
    return render_template('show_contact.html', data=data, error=error)


#############################################################
# STEP 4 -- define views to handle editing and creating new
# addresses for contacts.  You will also need to create view
# templates.
#############################################################
@app.route('/contacts/<contact_id>/address', methods=['GET', 'POST'])
def add_contact_address(contact_id):
    error = None
    if request.method == 'GET':
        return render_template('add_contact_address.html')

    contact = Contact.query.filter_by(id=contact_id).first()

    address_type = request.form['type'].lower()
    street = request.form['street']
    city = request.form['city']
    state = request.form['state']
    zip_code = request.form['zip']

    if not Address.is_valid_type(address_type):
        error = (
            "Invalid address type entered."
            "Must be 'home' or 'work'"
        )
        return render_template('add_contact_address.html', error=error)

    elif not Address.is_valid_form(street, city, state, zip_code):
        error = "Values cannot exceed 128 characters in length"
        return render_template('add_contact_address.html', error=error)

    address = Address(
        address_type=address_type,
        street=street,
        city=city,
        state=state,
        zip_code=zip_code
    )
    contact.addresses.append(address)
    db.session.commit()
    return redirect(url_for('show_contact', id=contact_id))


@app.route('/contacts/<contact_id>/addresses/<address_id>',
           methods=['GET', 'POST'])
def edit_contact_address(contact_id, address_id):
    error = None
    contact = Contact.query.filter_by(id=contact_id).first()
    address = contact.addresses.filter_by(id=address_id).first()

    if not contact or not address:
        abort(404)

    if request.method == 'GET':
        return render_template('edit_contact_address.html',
                               data=address.serialize())

    address_type = request.form['type'].lower()
    street = request.form['street']
    city = request.form['city']
    state = request.form['state']
    zip_code = request.form['zip']

    if not Address.is_valid_type(address_type):
        error = (
            "Invalid address type entered."
            "Must be 'home' or 'work'"
        )

        return render_template('edit_contact_address.html',
                               data=address.serialize(),
                               error=error)

    elif not Address.is_valid_form(street, city, state, zip_code):
        error = "Values cannot exceed 128 characters in length"
        return render_template('edit_contact_address.html',
                               data=address.serialize(),
                               error=error)

    address.address_type = address_type
    address.street = street
    address.city = city
    address.state = state
    address.zip_code = zip_code

    db.session.commit()
    return redirect(url_for('show_contact', id=contact_id))

# This causes a new database to be created when the app runs
bootstrap_database()

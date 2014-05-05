from flask import Flask, render_template, request
from cheap_ass_food import get_cheapest_food, make_delivery

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    addr = request.form['addr']
    city = request.form['city']
    zip_code = request.form['zip_code']
    em = request.form['em']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    phone = request.form['phone']
    state = request.form['state']
    card_number = request.form['card_number']
    card_cvc = request.form['card_cvc']
    card_expiry = request.form['card_expiry']
    card_bill_addr = request.form['card_bill_addr']
    card_bill_city = request.form['card_bill_city']
    card_bill_state = request.form['card_bill_state']
    card_bill_zip = request.form['card_bill_zip']
    card_bill_phone['card_bill_phone']

    return render_template('result.html')


if __name__ == '__main__':
    port = int(os.environ.get("PORT",5000))
    app.run(host='0.0.0.0', port=port, debug='true')


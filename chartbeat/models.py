from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON
#from .extensions import db
import datetime

db = SQLAlchemy()

class Host(db.Model):

    __tablename__ = 'host'
    id = db.Column(db.Integer, primary_key=True)
    api_key_id = db.Column(db.Integer, db.ForeignKey('api_key.id'))
    host_name = db.Column(db.String(255))
    created_at = db.Column(db.DateTime,
                           default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime)
    top_pages = db.Column(JSON)

    def __repr__(self):
        return '<Host ID%r>' % self.id

class ApiKey(db.Model):

    __tablename__ = 'api_key'
    id = db.Column(db.Integer, primary_key=True)
    api_key = db.Column(db.String(255))
    hosts = db.relationship(
        'Host', backref='api_key', lazy='dynamic'
    )

    def add_host(self, host_obj):
        self.hosts.append(host_obj)
        db.session.commit()
        return self

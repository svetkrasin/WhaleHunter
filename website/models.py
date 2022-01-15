from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Wallet(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	address = db.Column(db.String(10000))
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(150), unique=True)
	password = db.Column(db.String(150))
	nick = db.Column(db.String(150))
	wallets = db.relationship('Wallet')
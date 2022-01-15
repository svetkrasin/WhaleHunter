from crypt import methods
from curses import flash
from unicodedata import category
from urllib import request
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Wallet
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
	if request.method == 'POST':
		wallet = request.form.get('wallet')
		print(len(wallet))
		if len(wallet) != 42:
			flash('Wallet address is wrong!', category='error')
		else:
			new_wallet = Wallet(address=wallet, user_id=current_user.id)
			db.session.add(new_wallet)
			db.session.commit()
			flash('Wallet address added!', category='success')
	return render_template("home.html", user=current_user)

@views.route('/delete-wallet', methods=['POST'])
def delete_wallet():
	wallet = json.loads(request.data)
	walletId = wallet['walletId']
	wallet = Wallet.query.get(walletId)
	if wallet:
		if wallet.user_id == current_user.id:
			db.session.delete(wallet)
			db.session.commit()
	return jsonify({})
from flask import Blueprint, render_template
from flask_login import current_user
from .models import Wallet
from . import db
import json
from WhaleHunter import get_list_of_normal_transactions

transactions = Blueprint('transacitons', __name__)

@transactions.route('/<string:wallet_address>')
def wallet_transactions(wallet_address):
	wallet_transactions = get_list_of_normal_transactions(wallet_address)
	print(wallet_transactions[0])
	return render_template("wallet_transactions.html", user=current_user, wallet_address=wallet_address, transactions=wallet_transactions)
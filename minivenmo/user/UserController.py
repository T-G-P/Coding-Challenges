from .models import User
from ..creditcard.CreditCard import CreditCard
from .Database import db


class UserController:

    def add_user(self, name):
        new = True
        try:
            self.lookup_user(name, new)
        except Exception as e:
            print(e.message)
            return
        user = User(name)
        db.add_user(user)

    def add_credit_card(self, name, card_number):
        try:
            user = db.lookup_user(name)
            card_number = db.lookup_credit_card(user, card_number)
        except Exception as e:
            print(e.message)
            return
        try:
            CreditCard.validate_card(card_number)
        except Exception as e:
            print(e.message)
            return

        user.card_number = card_number
        db.database['credit_cards'].add(card_number)

    def display_balance(self, name):
        try:
            user = db.lookup_user(name)
        except Exception as e:
            print(e.message)
            return

        print('--$%.2f' % user.balance)

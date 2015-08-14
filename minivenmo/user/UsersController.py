import minivenmo.Database as Database
from .models import User, CreditCard


class UsersController:

    @staticmethod
    def add_user(name):
        new = True
        try:
            Database.db.lookup_user(name, new)
        except Exception as e:
            print(e.message)
            return

        user = User(name)
        try:
            Database.db.add_user(user)
        except AttributeError:
            pass

    @staticmethod
    def add_credit_card(name, card_number):
        try:
            user = Database.db.lookup_user(name)
            card_number = Database.db.lookup_credit_card(user, card_number)
        except Exception as e:
            print(e.message)
            return
        try:
            CreditCard.validate_card(card_number)
        except Exception as e:
            print(e.message)
            return

        user.card_number = card_number
        Database.db.database['credit_cards'].add(card_number)

    @staticmethod
    def display_balance(name):
        try:
            user = Database.db.lookup_user(name)
        except Exception as e:
            print(e.message)
            return

        print('--$%.2f' % user.balance)

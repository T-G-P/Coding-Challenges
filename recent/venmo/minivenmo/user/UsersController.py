import minivenmo.Database as Database
from .models import User, CreditCard


class UsersController:

    @staticmethod
    def add_user(name):
        new = True
        try:
            User.validate_name(name)
        except Exception as e:
            raise

        try:
            Database.db.lookup_user(name, new)
        except Exception as e:
            raise

        user = User(name)
        try:
            Database.db.add_user(user)
        except AttributeError:
            pass
        return True

    @staticmethod
    def add_credit_card(name, card_number):
        try:
            user = Database.db.lookup_user(name)
            card_number = Database.db.lookup_credit_card(user, card_number)
        except Exception as e:
            raise

        try:
            CreditCard.validate_card(card_number)
        except Exception as e:
            raise

        user.card_number = card_number
        Database.db.database['credit_cards'].add(card_number)
        return True

    @staticmethod
    def display_balance(name):
        try:
            user = Database.db.lookup_user(name)
        except Exception as e:
            raise

        print('-- $%.2f' % user.balance)
        return True

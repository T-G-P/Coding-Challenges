import minivenmo.Database as Database
from .models import Transaction


class TransactionsController:

    @staticmethod
    def create_transaction(actor_name, target_name, amount, *note):
        try:
            actor, target = tuple(map(Database.db.lookup_user,
                                      [actor_name, target_name]))
        except Exception as e:
            print(e.message)
            return False

        payment_note = ' '.join(note)
        if actor is target:
            raise Exception("ERROR: users cannot pay themselves")
        try:
            float_amount = float(amount.split('$')[-1])
            if float_amount < 0:
                raise ValueError
        except ValueError:
            raise Exception("ERROR: Invalid Amount Entered")

        if not actor.card_number:
            raise Exception("ERROR: this user does not have a credit card")

        target.balance += float_amount
        transaction = Transaction(actor_name, target_name,
                                  float_amount, payment_note)
        Database.db.add_transaction(transaction)
        return True

    @staticmethod
    def display_feed(name):
        try:
            user = Database.db.lookup_user(name)
        except Exception as e:
            print(e.message)
            return False

        transactions = Database.db.lookup_transactions(name)
        if transactions:
            for transaction in transactions:
                if transaction.actor == user.name:
                    print('-- You paid %s $%.2f for %s' % (transaction.target,
                                                           transaction.amount,
                                                           transaction.note))
                elif transaction.target == user.name:
                    print('-- %s paid you $%.2f for %s' % (transaction.actor,
                                                           transaction.amount,
                                                           transaction.note))
        return True

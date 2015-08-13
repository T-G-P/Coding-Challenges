from .Database import db
from .models import Transaction


class TransactionController:

    def create_transaction(self, actor_name, target_name, amount, *note):
        try:
            actor, target = tuple(map(db.lookup_user,
                                      [actor_name, target_name]))
        except Exception as e:
            print(e.message)
            return

        payment_note = ' '.join(note)
        if actor is target:
            raise Exception("ERROR: users cannot pay themselves")
        try:
            float_amount = float(amount.split('$')[-1])
        except ValueError:
            raise Exception("ERROR: Invalid Amount Entered")
        if float_amount < 0:
            raise Exception("ERROR: Can't have negative amount")

        if not self.card_number:
            raise Exception("ERROR: this user does not have a credit card")

        target.balance += float_amount
        transaction = Transaction(actor_name, target_name,
                                  float_amount, payment_note)
        db.add_transaction(transaction)

    def get_feed(self, name):
        try:
            user = db.lookup_user(name)
        except Exception as e:
            print(e.message)
            return

        transactions = db.lookup_transactions(name)
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

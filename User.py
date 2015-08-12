import string
from Transaction import Transaction


class User:

    def __init__(self, name):
        try:
            User.validate_name(name)
        except Exception as e:
            print e.message
            return
        self.name = name
        self.card_number = None
        self.feed = []
        self.transactions = []
        self.balance = 0.00

    @staticmethod
    def validate_name(name):
        valid_chars = string.ascii_letters+string.digits+'_-'
        if len(name) < 4 or len(name) > 15:
            raise Exception("ERROR: Invalid length for name: %s" % name)
        elif not any({c for c in name if c in valid_chars}):
            raise Exception("ERROR: Invalid length for name: %s" % name)
        return True

    def set_card_number(self, card_number):
        # credit card wll already be  processed before set
        self.card_number = card_number

    def pay(self, target, amount, note):
        actor = self
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

        transaction = Transaction(actor, target, float_amount, note)
        transaction.update_feeds()
        self.transactions.append(transaction)
        target.transactions.append(transaction)
        target.balance += float_amount

    def get_feed(self):
        for payment in self.feed[::-1]:
            print payment

    def get_balance(self):
        print '--$%.2f' % self.balance

import string
# from Transaction import Transaction


class User:

    name = None
    card_number = None
    feed = []
    balance = 0.00

    def __init__(self, name):
        if User.validate_name(name):
            self.name = name

    @staticmethod
    def validate_name(name):
        valid_chars = string.ascii_letters+string.digits+'_-'
        if len(name) < 4 or len(name) > 15:
            raise Exception("Invalid length for name: %s" % name)
        elif not any({c for c in name if c in valid_chars}):
            raise Exception("Invalid length for name: %s" % name)
        return True

    def set_card_number(self, card_number):
        # credit card wll already be  processed before set
        self.card_number = card_number

    def pay(self, target, amount, note):
        # create transaction, process it, then add to both users feeds
        # transaction = Transaction(self, target, amount, note)
        if self is target:
            raise "Cannot pay themselves"
        if amount < 0:
            raise "Cannot have negative amount"
        if not self.credit_card:
            raise "Can't pay without credit card"

        self.feed.append('--You paid %s $%.2f for %s' % (target, amount, note))
        target.feed.append('--%s paid you $%.2f for %s' % (self, amount, note))
        target.balance += amount

    def get_balance(self):
        return '--$%.2f' % self.balance

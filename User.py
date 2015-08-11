import string
# from Transaction import Transaction


class User:

    name = None
    card_number = None
    feed = []
    balance = 0.00

    def __init__(self, name):
        try:
            User.validate_name(name)
        except Exception as e:
            print e.message
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
        if self.card_number:
            raise Exception("ERROR: this user already has a valid credit card")
            return
        self.card_number = card_number

    def pay(self, target, amount, note):
        # create transaction, process it, then add to both users feeds
        # transaction = Transaction(self, target, amount, note)
        if self is target:
            raise Exception("ERROR: users cannot pay themselves")
        elif amount < 0:
            raise Exception("ERROR: Invalid amount")
        elif not self.credit_card:
            raise Exception("ERROR: this user does not have a credit card")
        elif type(amount) is not float:
            raise Exception("ERROR: Invalid amount entered")

        self.feed.append('--You paid %s $%.2f for %s' % (target, amount, note))
        target.feed.append('--%s paid you $%.2f for %s' % (self, amount, note))
        target.balance += amount

    def get_balance(self):
        return '--$%.2f' % self.balance

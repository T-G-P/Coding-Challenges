class User:

    name = None
    credit_card = None
    feed = []
    balance = 0.00

    def __init__(self, name):
        if User.is_valid_name(name):
            self.name = name

    @staticmethod
    def is_valid_name(name):
        pass

    def set_credit_card(self, credit_card):
        #credit card wll already be  processed before set
        pass

    def add_transaction(self, transaction):
        self.feed.append(transaction)

    def pay(self, name, amount, note):
        #create transaction, process it, then add to both users feeds
        pass

    def get_balance(self):
        return self.balance


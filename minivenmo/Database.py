from .user.User import User


class Database:

    users = {}
    credit_cards = set()
    transactions = {}

    def lookup_user(self, name, new=False):
        if new and name in self.users.keys():
            raise Exception("ERROR: This user: %s already exists" % name)
        elif not new and name not in self.users.keys():
            raise Exception("ERROR: This user: %s doesn't exist" % name)
        return self.users.get(name)

    def lookup_credit_card(self, user, card_number):
        if user.card_number or user.card_number == card_number:
            raise Exception("ERROR: this user already has a valid credit card")
        elif card_number in self.credit_cards:
            raise Exception("ERROR: that card number has already been added by"
                            " another user, reported for fraud!")
        return card_number

    def add_user(self, name):
        user = User(name)
        self.users[name] = user

    def add_credit_card(self, name, card_number):
        self.credit_cards.add(card_number)

db = Database()

class Database:

    database = {
        'users': {},
        'credit_cards': set(),
        'transactions': {}
    }

    def clear_db(self):
        for key in self.database.keys():
            self.database[key].clear()

    def lookup_user(self, name, new=False):
        if new and name in self.database['users'].keys():
            raise Exception("ERROR: This user: %s already exists" % name)
        elif not new and name not in self.database['users'].keys():
            raise Exception("ERROR: This user: %s doesn't exist" % name)
        return self.database['users'].get(name)

    def lookup_credit_card(self, user, card_number):
        if user.card_number or user.card_number == card_number:
            raise Exception("ERROR: this user already has a valid credit card")
        elif card_number in self.database['credit_cards']:
            raise Exception("ERROR: that card number has already been added by"
                            " another user, reported for fraud!")
        return card_number

    def lookup_transactions(self, name):
        return self.database['transactions'].get(name)

    def add_user(self, user):
        self.database['users'][user.name] = user
        return user

    def add_credit_card(self, card_number):
        self.database['credit_cards'].add(card_number)
        return card_number

    def add_transaction(self, transaction):
        actor = transaction.actor
        target = transaction.target
        if all([
                self.database['transactions'].get(actor),
                self.database['transactions'].get(target)
                ]):
            self.database['transactions'][actor].append(transaction)
            self.database['transactions'][target].append(transaction)
        else:
            self.database['transactions'][actor] = [transaction]
            self.database['transactions'][target] = [transaction]


def init_db():
    global db
    db = Database()

import string


class User:

    def __init__(self, name):
            try:
                User.validate_name(name)
            except Exception as e:
                print(e.message)
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

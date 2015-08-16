import string


class User:

    def __init__(self, name):
        self.name = name
        self.card_number = None
        self.feed = []
        self.transactions = []
        self.balance = 0.00

    @staticmethod
    def validate_name(name):
        # replace validation with regex
        valid_chars = string.ascii_letters+string.digits+'_-'
        if len(name) < 4 or len(name) > 15:
            raise Exception("ERROR: Invalid length for name: %s" % name)
        elif not all({c in valid_chars for c in name}):
            raise Exception("ERROR: Invalid characters for name: %s" % name)
        return True

class CreditCard:

    # Luhn-10 validator taken from wiki page on algorithm
    @staticmethod
    def luhn_checksum(card_number):
        def digits_of(n):
            return [int(d) for d in str(n)]
        try:
            digits = digits_of(card_number)
        except ValueError:
            raise Exception("ERROR: This card is invalid")

        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]

        checksum = sum(odd_digits)
        for d in even_digits:
            checksum += sum(digits_of(d*2))
        return checksum % 10

    @staticmethod
    def is_luhn_valid(card_number):
        return CreditCard.luhn_checksum(card_number) == 0

    @staticmethod
    def validate_card(card_number):
        if all(
            [
                CreditCard.is_luhn_valid(card_number),
                len(card_number) <= 19
            ]
        ):
            return True
        else:
            raise Exception("ERROR: This card is invalid")

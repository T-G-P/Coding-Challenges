class CreditCard:

    card_number = None

    def __init__(self, card_number):
        if len(card_number) > 19:
            raise "Invalid Credit Card"
        if not CreditCard.is_luhn_valid(card_number):
            raise "Invalid Credit Card"
        self.card_number = card_number

    # Luhn-10 validator taken from wiki page on algorithm
    @staticmethod
    def luhn_checksum(card_number):
        def digits_of(n):
            return [int(d) for d in str(n)]
        digits = digits_of(card_number)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]

        checksum = sum(odd_digits)
        for d in even_digits:
            checksum += sum(digits_of(d*2))
        return checksum % 10

    @staticmethod
    def is_luhn_valid(card_number):
        return CreditCard.luhn_checksum(card_number) == 0

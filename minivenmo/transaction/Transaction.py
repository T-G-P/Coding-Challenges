class Transaction:

    def process_transaction(self, actor, target, amount, note):
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
        return

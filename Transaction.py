class Transaction:

    actor = None
    target = None
    amount = None
    note = None

    def __init__(self, actor, target, amount, note):
        if actor is target:
            raise "Cannot pay themselves"
        if amount < 0:
            raise "Cannot have negative amount"
        if not actor.credit_card:
            raise "Can't pay without credit card"

        self.actor = actor
        self.target = target
        self.amount = amount
        self.note = note

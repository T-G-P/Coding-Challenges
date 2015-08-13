class Transaction:

    def __init__(self, actor_name, target_name, amount, note):
        self.actor = actor_name
        self.target = target_name
        self.amount = amount
        self.note = note

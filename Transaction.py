class Transaction:

    actor = None
    target = None
    amount = None
    note = None

    def __init__(self, actor, target, amount, note):
        self.actor = actor
        self.target = target
        self.amount = amount
        self.note = note

    def update_feeds(self):
        self.actor.feed.append('--You paid %s $%.2f for %s' % (self.target, float_amount, note))
        self.target.feed.append('--%s paid you $%.2f for %s' % (self.actor, float_amount, note))

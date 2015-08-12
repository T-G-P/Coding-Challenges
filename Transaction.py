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
        print(self.actor.name, self.target.name)
        self.actor.feed.append('--You paid %s $%.2f for %s' % (self.target.name, self.amount, self.note))
        self.target.feed.append('--%s paid you $%.2f for %s' % (self.actor.name, self.amount, self.note))

import argparse

class MiniVenmo():

    users = {}
    credit_cards = {}
    transactions = []

    def lookup_user(self, name, new=False):
        if new and name in self.users.keys():
            raise Exception("ERROR: This user: %s already exists" % name)
        elif name not in self.users.keys():
            raise Exception("ERROR: This user: %s doesn't exist" % name)
        return True

    def lookup_credit_card(self, card_number):
        if card_number in credit_cards:
            raise Exception("ERROR: that card number has already been added by"
                            " another user, reported for fraud!")
            return
        return True

    def add_user(self, name):
        try:
            self.lookup_user(name, new=True)
        except Exception as e:
            print e.message
            return
        user = User(name)
        self.users['name'] = user

    def add_credit_card(self, name, card_number):
        try:
            self.lookup_user(name)
            self.lookup_credit_card(card_number)
        except Exception as e:
            print e.message
            return
        user = users[name]
        try:
            CreditCard.validate_card(card_number)
        except Exception as e:
            print e.message
        user.set_card_number(card_number)
        credit_cards.add(card_number)

    def pay_user(self, actor, target, amount, *note):
        try:
            map(self.lookup_user, [actor, target])
        except Exception as e:
            print e.message
            return
        actor_user = users[actor]
        target_user = users[target]
        float_amount = amount
        payment_note = ' '.join(note)
        try:
            actor_user.pay(target_user, float_amount, payment_note)
        except Exception as e:
            print e.message
        return

    def display_feed(self, name):
        try:
            self.lookup_user(name)
        except Exception as e:
            print e.message
            return
        user = users[name]
        print user.get_feed()
        return

    def display_balance(self, name):
        try:
            self.lookup_user(name)
        except Exception as e:
            print e.message
            return
        user = users[name]
        print user.get_balance()
        return

    def process_args(args):
        choices = ['user', 'add', 'pay', 'feed', 'balance']
        if not args or len(args) < 2:
            raise Exception("ERROR: invalid arguments")
        elif args[0] not in choices:
            raise Exception("ERROR: command not recognized")
        elif args[0].lower() == 'user' and len(args) == 2:
            add_user(*args[1:])
        elif args[0].lower() == 'add' and len(args) == 3:
            add_credit_card(*args[1:])
        elif args[0].lower() == 'pay' and len(args) == 5:
            pay_user(*args[1:])
        elif args[0].lower() == 'feed' and len(args) == 2:
            display_feed(*args[1:])
        elif args[0].lower() == 'balance' and len(args) == 2:
            display_balance(*args[1:])
        else:
            self.usage()

    def process_file(self, file_obj):
        for command in file_ob:
            try:
                self.process_args(line.split(' '))
            except Exception as e:
                print e.message
        return

    def usage(self):
        print '\nUsage: MOVE X ONTO Y. ex: MOVE 4 ONTO 1\n'
        print 'Enter a command or press q or Q to quit\n'
        print 'Type \'help\' for usage info'
        return

    def run():
        parser = argparse.ArgumentParser(description='MiniVenmo')
        parser.add_argument('filename', nargs='?', type=argparse.FileType('r'))
        args = parser.parse_args()

        if args.filename:
            process_file(args.filename)
            return

        while True:
            args = raw_input('> ').split()
            if args[0].lower() == 'q':
                print 'Exiting...\n'
                return
            elif args[0].lower() == 'help':
                self.usage()
                return

            try:
                self.process_args(line.split(' '))
            except Exception as e:
                print e.message

        return

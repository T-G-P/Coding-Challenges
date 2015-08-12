import argparse
from .creditcard.CreditCard import CreditCard
from .user.User import User

class MiniVenmo:

    users = {}
    credit_cards = set()

    def lookup_user(self, name, new=False):
        if new and name in self.users.keys():
            raise Exception("ERROR: This user: %s already exists" % name)
        elif not new and name not in self.users.keys():
            raise Exception("ERROR: This user: %s doesn't exist" % name)
        return True

    def lookup_credit_card(self, user, card_number):
        if user.card_number or user.card_number == card_number:
            raise Exception("ERROR: this user already has a valid credit card")
        elif card_number in self.credit_cards:
            raise Exception("ERROR: that card number has already been added by"
                            " another user, reported for fraud!")
        return True

    def add_user(self, name):
        try:
            self.lookup_user(name, True)
        except Exception as e:
            print e.message
            return
        user = User(name)
        self.users[name] = user

    def add_credit_card(self, name, card_number):
        try:
            self.lookup_user(name)
            user = self.users[name]
            self.lookup_credit_card(user, card_number)
        except Exception as e:
            print e.message
            return
        try:
            CreditCard.validate_card(card_number)
        except Exception as e:
            print e.message
            return
        user.set_card_number(card_number)
        self.credit_cards.add(card_number)

    def pay_user(self, actor_name, target_name, amount, *note):
        try:
            map(self.lookup_user, [actor_name, target_name])
        except Exception as e:
            print e.message
            return
        actor_user = self.users[actor_name]
        target_user = self.users[target_name]
        payment_note = ' '.join(note)
        try:
            actor_user.pay(target_user, amount, payment_note)
        except Exception as e:
            print e.message
        return

    def display_feed(self, name):
        try:
            self.lookup_user(name)
        except Exception as e:
            print e.message
            return
        user = self.users[name]
        user.get_feed()
        return

    def display_balance(self, name):
        try:
            self.lookup_user(name)
        except Exception as e:
            print e.message
            return
        user = self.users[name]
        user.get_balance()
        return

    def process_args(self, args):
        choices = ['user', 'add', 'pay', 'feed', 'balance']
        if not args or all([len(args) < 2, args[0] in choices]):
            raise Exception("ERROR: invalid arguments")
        elif args[0] not in choices:
            raise Exception("ERROR: command not recognized")
        elif args[0].lower() == 'user' and len(args) == 2:
            self.add_user(*args[1:])
        elif args[0].lower() == 'add' and len(args) == 3:
            self.add_credit_card(*args[1:])
        elif args[0].lower() == 'pay' and len(args) >= 5:
            self.pay_user(*args[1:])
        elif args[0].lower() == 'feed' and len(args) == 2:
            self.display_feed(*args[1:])
        elif args[0].lower() == 'balance' and len(args) == 2:
            self.display_balance(*args[1:])
        else:
            raise Exception("ERROR: invalid arguments")

    def process_file(self, file_name):
        with open(file_name) as f:
            for line in f:
                args = line.replace('\n', '').split()
                try:
                    self.process_args(args)
                except Exception as e:
                    print e.message
        return

    def usage(self):
        print ('\nUsage:\nuser <user>'
               '\nadd <user> <card_number>'
               '\npay <actor> <target> <amount> <note>'
               '\nfeed <user>'
               '\nbalance <user>'
               '\nHelp: type help to repeat this message'
               '\nQuit: type Q or q to quit')
        return

    def run(self):
        parser = argparse.ArgumentParser(description='MiniVenmo')
        parser.add_argument('filename', nargs='?')
        args = parser.parse_args()

        if args.filename:
            self.process_file(args.filename)
            return

        self.usage()
        while True:
            args = raw_input('> ').split()
            if args[0].lower() == 'q':
                print 'Exiting...\n'
                return
            elif args[0].lower() == 'help':
                self.usage()
                continue
            try:
                self.process_args(args)
            except Exception as e:
                print e.message
        return

if __name__ == "__main__":
    test = MiniVenmo()
    test.run()

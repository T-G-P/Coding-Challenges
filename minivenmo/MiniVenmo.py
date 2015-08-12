import argparse
from .creditcard.CreditCard import CreditCard
from .Database import db


class MiniVenmo:

    def add_user(self, name):
        new = True
        try:
            self.lookup_user(name, new)
        except Exception as e:
            print(e.message)
            return
        db.add_user(name)

    def add_credit_card(self, name, card_number):
        try:
            user = db.lookup_user(name)
            card_number = db.lookup_credit_card(user, card_number)
        except Exception as e:
            print(e.message)
            return
        try:
            CreditCard.validate_card(card_number)
        except Exception as e:
            print(e.message)
            return
        user.set_card_number(card_number)
        self.credit_cards.add(card_number)

    def pay_user(self, actor_name, target_name, amount, *note):
        try:
            actor_user, target_user = tuple(map(db.lookup_user,
                                                [actor_name, target_name]))
        except Exception as e:
            print(e.message)
            return
        payment_note = ' '.join(note)
        try:
            actor_user.pay(target_user, amount, payment_note)
        except Exception as e:
            print(e.message)
        return

    def display_feed(self, name):
        try:
            self.lookup_user(name)
        except Exception as e:
            print(e.message)
            return
        user = self.users[name]
        user.get_feed()
        return

    def display_balance(self, name):
        try:
            self.lookup_user(name)
        except Exception as e:
            print(e.message)
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
                    print(e.message)
        return

    def usage(self):
        print('\nUsage:\nuser <user>'
              '\nHelp: type help to repeat this message'
              '\nQuit: type Q or q to quit\n'
              '\nadd <user> <card_number>'
              '\npay <actor> <target> <amount> <note>'
              '\nfeed <user>'
              '\nbalance <user>')
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
            args = input('> ').split()
            if args[0].lower() == 'q':
                print('Exiting...\n')
                return
            elif args[0].lower() == 'help':
                self.usage()
                continue
            try:
                self.process_args(args)
            except Exception as e:
                print(e.message)
        return

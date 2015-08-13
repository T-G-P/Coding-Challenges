import argparse
import Database
from .user.UserController import UserController
from .transaction.TransactionController import TransactionController


class MiniVenmo:

    def process_args(self, args):
        choices = ['user', 'add', 'pay', 'feed', 'balance']
        if not args or all([len(args) < 2, args[0] in choices]):
            raise Exception("ERROR: invalid arguments")
        elif args[0] not in choices:
            raise Exception("ERROR: command not recognized")
        elif args[0].lower() == 'user' and len(args) == 2:
            UserController.add_user(*args[1:])
        elif args[0].lower() == 'add' and len(args) == 3:
            UserController.add_credit_card(*args[1:])
        elif args[0].lower() == 'pay' and len(args) >= 5:
            TransactionController.create_transaction(*args[1:])
        elif args[0].lower() == 'feed' and len(args) == 2:
            TransactionController.display_feed(*args[1:])
        elif args[0].lower() == 'balance' and len(args) == 2:
            UserController.display_balance(*args[1:])
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
        Database.init_db()
        parser = argparse.ArgumentParser(description='MiniVenmo')
        parser.add_argument('filename', nargs='?')
        args = parser.parse_args()

        if args.filename:
            self.process_file(args.filename)
            return

        try:
            input = raw_input
        except NameError:
            pass

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

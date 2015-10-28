import argparse
from minivenmo import Database
from .user.UsersController import UsersController
from .transaction.TransactionsController import TransactionsController


class MiniVenmo:

    def __process_args(self, args):
        choices = ['user', 'add', 'pay', 'feed', 'balance']
        if not args or all([len(args) < 2, args[0] in choices]):
            raise Exception("ERROR: invalid arguments")
        elif args[0] not in choices:
            raise Exception("ERROR: command not recognized")
        elif args[0].lower() == 'user' and len(args) == 2:
            UsersController.add_user(*args[1:])
        elif args[0].lower() == 'add' and len(args) == 3:
            UsersController.add_credit_card(*args[1:])
        elif args[0].lower() == 'pay' and len(args) >= 5:
            TransactionsController.create_transaction(*args[1:])
        elif args[0].lower() == 'feed' and len(args) == 2:
            TransactionsController.display_feed(*args[1:])
        elif args[0].lower() == 'balance' and len(args) == 2:
            UsersController.display_balance(*args[1:])
        else:
            raise Exception("ERROR: invalid arguments")
        return True

    def __process_file(self, file_name):
        try:
            with open(file_name) as f:
                for line in f:
                    stripped_line = line.rstrip('\n')
                    print(stripped_line)

                    args = stripped_line.split()
                    try:
                        self.__process_args(args)
                    except Exception as e:
                        print(e.message)
        except IOError:
            raise
        return True

    def __usage(self):
        print('\nUsage:\nuser <user>'
              '\nHelp: type help to repeat this message'
              '\nQuit: type Q or q to quit\n'
              '\nadd <user> <card_number>'
              '\npay <actor> <target> <amount> <note>'
              '\nfeed <user>'
              '\nbalance <user>')
        return True

    def run(self):
        Database.init_db()
        parser = argparse.ArgumentParser(description='MiniVenmo')
        parser.add_argument('filename', nargs='?')
        args = parser.parse_args()

        if args.filename:
            self.__process_file(args.filename)
            return True

        self.__usage()
        while True:
            args = raw_input('> ').split()
            if args[0].lower() == 'q':
                print('Exiting...\n')
                return True
            elif args[0].lower() == 'help':
                self.__usage()
                continue
            try:
                self.__process_args(args)
            except Exception as e:
                print(e.message)
        return True

import argparse
# args: user, add, pay, feed, balance


class MiniVenmo:
    # do object instantiation here for User, Transaction, CreditCard

    users = {}  # i.e {'Tobias': tobias_obj}
    credit_cards = {}  # set of credit cards
    transactions = []

    def add_user(command):
        pass

    def add_credit_card(command):
        pass

    def pay_user(command):
        pass

    def display_feed(command):
        pass

    def display_balance(command):
        pass

    def read_file(self, file_name):
        with open(file_name) as f:
            for line in f:
                # use argeparse
                self.process_command(line.split(' '))

    def run():
        # if only one argument, interactive, otherwise read from file
        #
        parser = argparse.ArgumentParser(description='MiniVenmo')
        parser.add_argument('arg',
                            choices=['user', 'add', 'pay', 'feed', 'balance'])
        parser.add_argument('filename', nargs=1, type=argparse.FileType('r'))

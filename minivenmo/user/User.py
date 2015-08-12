import string
from .models import User
# from ..transaction.Transaction import Transaction


class UserController:

    # def __update_feed(self, feed_note):
    #     self.feed.append(feed_note)

    def set_card_number(self, card_number):
        # credit card wll already be  processed before set
        self.card_number = card_number

    # def pay(self, target, amount, note):
    #     actor = self
    #     if actor is target:
    #         raise Exception("ERROR: users cannot pay themselves")
    #     try:
    #         float_amount = float(amount.split('$')[-1])
    #     except ValueError:
    #         raise Exception("ERROR: Invalid Amount Entered")
    #     if float_amount < 0:
    #         raise Exception("ERROR: Can't have negative amount")

    #     if not self.card_number:
    #         raise Exception("ERROR: this user does not have a credit card")

    #     actor_feed = '-- You paid %s $%.2f for %s' % (target.name,
    #                                                   float_amount, note)

    #     target_feed = '-- %s paid you $%.2f for %s' % (actor.name,
    #                                                    float_amount, note)

    #     list(map(self.__update_feed, [(self, actor_feed),
    #                                   (target, target_feed)]))

    def get_feed(self):
        for payment in self.feed:
            print(payment)

    def get_balance(self):
        print('--$%.2f' % self.balance)

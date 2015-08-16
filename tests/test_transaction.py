import unittest
from minivenmo.user.UsersController import UsersController
from minivenmo.transaction.TransactionsController import (
    TransactionsController, Database
)

class TestTransactionsController(unittest.TestCase):

    def test_create_transaction(self):
        Database.db.clear_db()
        valid_card = "4111111111111111"
        invalid_card = "12345678910111213"
        note = "This is a test note"
        valid_amount = '$66.60'
        invalid_amount = '66F.60'
        invalid_amount2 = '$-66.60'

        actor_username = "Tobias-P_88"
        target_username = 'test_user'
        dne_username = 'DNE1'

        UsersController.add_user(actor_username)
        UsersController.add_user(target_username)
        UsersController.add_credit_card(actor_username, valid_card)

        # A valid transaction. Check to see the balance
        # incremented  Also check to see that the transaction
        # is stored for both users
        target = Database.db.lookup_user(target_username)
        old_balance = target.balance
        self.assertTrue(
            TransactionsController.create_transaction(
                actor_username, target_username, valid_amount, note
            )
        )
        float_amount = float(valid_amount.split('$')[-1])
        self.assertEqual(target.balance-old_balance, float_amount)

        actor_trans, target_trans = tuple(map(
            Database.db.lookup_transactions,
            [actor_username, target_username]
        ))

        total_transactions = list(set(actor_trans).union(set(target_trans)))
        transaction = list({
            transaction for transaction in total_transactions
            if all(
                [
                    transaction.actor == actor_username,
                    transaction.target == target_username,
                    transaction.amount == float_amount,
                    transaction.note == note
                ]
            )})
        # Checking to see that the transaction exists for both users
        self.assertIn(transaction[0], actor_trans)
        self.assertIn(transaction[0], target_trans)

        # Nonexistant user trying to pay
        with self.assertRaises(Exception) as cm:
            TransactionsController.create_transaction(
                dne_username, target_username, valid_amount, note
            )
        exception = cm.exception
        self.assertIn("doesn't exist", exception.message)

        # Paying themselves
        with self.assertRaises(Exception) as cm:
            TransactionsController.create_transaction(
                actor_username, actor_username, valid_amount, note
            )
        exception = cm.exception
        self.assertEqual(exception.message, "ERROR: users cannot pay themselves")

        # Paying without credit card
        with self.assertRaises(Exception) as cm:
            TransactionsController.create_transaction(
                target_username, actor_username, valid_amount, note
            )
        exception = cm.exception
        self.assertEqual(exception.message, "ERROR: this user does not have a credit card")

        # invalid amount passed
        with self.assertRaises(Exception) as cm:
            TransactionsController.create_transaction(
                actor_username, target_username, invalid_amount, note
            )
        exception = cm.exception
        self.assertEqual(exception.message, "ERROR: Invalid Amount Entered")

        # a negative amount passed
        with self.assertRaises(Exception) as cm:
            TransactionsController.create_transaction(
                actor_username, target_username, invalid_amount2, note
            )
        exception = cm.exception
        self.assertEqual(exception.message, "ERROR: Invalid Amount Entered")


    def test_display_feed(self):
        Database.db.clear_db()
        valid_card = "4111111111111111"
        valid_card = "4111111111111111"
        note = "This is a test note"
        valid_amount = '$66.60'

        actor_username = "Tobias-P_88"
        target_username = 'test_user'
        dne_username = 'DNE1'

        UsersController.add_user(actor_username)
        UsersController.add_user(target_username)
        UsersController.add_credit_card(actor_username, valid_card)
        TransactionsController.create_transaction(
            actor_username, target_username, valid_amount, note
        )

        # Display feed should return true for both users
        # If True, the feeds get printed to the screen
        self.assertTrue(
            TransactionsController.display_feed(actor_username)
        )
        self.assertTrue(
            TransactionsController.display_feed(target_username)
        )

        # Nonexistant user trying to get feed
        with self.assertRaises(Exception) as cm:
            TransactionsController.display_feed(dne_username)
        exception = cm.exception
        self.assertIn("doesn't exist", exception.message)

if __name__ == '__main__':
    unittest.main()

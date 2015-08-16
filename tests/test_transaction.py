import unittest
from minivenmo.user.UsersController import UsersController
from minivenmo.transaction.TransactionsController import (
    TransactionsController, Database
)

class TestTransactionsController(unittest.TestCase):

    def test_create_transaction(self):
        print 'in create transaction'
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
        UsersController.add_credit_card(target_username, invalid_card)

        # A valid transaction
        self.assertTrue(
            TransactionsController.create_transaction(
                actor_username, target_username, valid_amount, note
            )
        )

        # Nonexistant user trying to pay
        self.assertFalse(
            TransactionsController.create_transaction(
                dne_username, target_username, valid_amount, note
            )
        )

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

        Database.db.clear_db()

    def test_display_feed(self):
        print 'in display feed'
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
        self.assertTrue(TransactionsController.display_feed(actor_username))
        self.assertTrue(TransactionsController.display_feed(target_username))

        # feed will throw exception and return false for invalid users
        self.assertFalse(TransactionsController.display_feed(dne_username))

        Database.db.clear_db()

if __name__ == '__main__':
    unittest.main()

import unittest
from minivenmo.user.UsersController import UsersController, Database


class TestUsersController(unittest.TestCase):
    def test_add_user(self):
        Database.db.clear_db()
        test_username = "Tobias-P_88"
        invalid_user = "Tobias!@#$%^&*"
        invalid_user2 = 'abc'

        # Add a new valid user and expect no problems
        self.assertTrue(UsersController.add_user(test_username))
        user = Database.db.lookup_user(test_username)
        self.assertEqual(test_username, user.name)

        # Add invalid characters username
        with self.assertRaises(Exception) as cm:
            UsersController.add_user(invalid_user)
        exception = cm.exception
        self.assertIn("Invalid characters", exception.message)

        # Add invalid length username
        with self.assertRaises(Exception) as cm:
            UsersController.add_user(invalid_user2)
        exception = cm.exception
        self.assertIn("Invalid length", exception.message)

        # Add an existing user
        with self.assertRaises(Exception) as cm:
            UsersController.add_user(test_username)
        exception = cm.exception
        self.assertIn("already exists", exception.message)


    def test_add_credit_card(self):
        Database.db.clear_db()
        valid_card = "4111111111111111"
        invalid_card = "A12345678910111213"

        test_username = "Tobias-P_88"
        test_username2 = 'test_user'
        dne_username = 'DNE1'

        UsersController.add_user(test_username)
        UsersController.add_user(test_username2)
        user1 = Database.db.lookup_user(test_username)
        user2 = Database.db.lookup_user(test_username2)

        # Add invalid card to existing user
        with self.assertRaises(Exception) as cm:
            UsersController.add_credit_card(test_username, invalid_card)
        exception = cm.exception
        self.assertEqual("ERROR: This card is invalid", exception.message)
        self.assertNotEqual(user1.card_number, invalid_card)

        # Add valid card to existing user
        self.assertTrue(UsersController.add_credit_card(test_username,
                                                        valid_card))
        self.assertEqual(user1.card_number, valid_card)

        # Add a valid card to a user that already has a card
        with self.assertRaises(Exception) as cm:
            UsersController.add_credit_card(test_username, valid_card)
        exception = cm.exception
        self.assertEqual(
            "ERROR: this user already has a valid credit card",
            exception.message
        )

        # Add valid card that belongs to someone else
        with self.assertRaises(Exception) as cm:
            UsersController.add_credit_card(test_username2, valid_card)
        exception = cm.exception
        self.assertEqual(
            ("ERROR: that card number has already been added by"
             " another user, reported for fraud!"),
            exception.message
        )
        self.assertNotEqual(user2.card_number, valid_card)

        # Add a valid card to a user that isn't in the database
        with self.assertRaises(Exception) as cm:
            UsersController.add_credit_card(dne_username, valid_card)
        exception = cm.exception
        self.assertIn("doesn't exist", exception.message)

    def test_display_balance(self):
        Database.db.clear_db()
        test_username = "Tobias-P_88"
        dne_username = 'DNE1'

        UsersController.add_user(test_username)
        # Make call to display balance method and should return True
        self.assertTrue(UsersController.display_balance(test_username))

        # Try to get balance for user that doesn't exist
        with self.assertRaises(Exception) as cm:
            UsersController.display_balance(dne_username)
        exception = cm.exception
        self.assertIn("doesn't exist", exception.message)


if __name__ == '__main__':
    unittest.main()

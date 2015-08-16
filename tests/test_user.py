import unittest
from minivenmo.user.UsersController import UsersController, Database


class TestUserController(unittest.TestCase):
    def test_add_user(self):
        test_username = "Tobias-P_88"
        invalid_user = "Tobias!@#$%^&*"
        invalid_user2 = 'abc'

        # Add a user user and expect no problems
        self.assertTrue(UsersController.add_user(test_username))

        # Add invalid characters username
        self.assertFalse(UsersController.add_user(invalid_user))

        # Add invalid length username
        self.assertFalse(UsersController.add_user(invalid_user2))

        # Add an existing user
        self.assertFalse(UsersController.add_user(test_username))
        Database.db.clear_db()

    def test_add_credit_card(self):
        valid_card = "4111111111111111"
        invalid_card = "12345678910111213"

        test_username = "Tobias-P_88"
        test_username2 = 'test_user'
        dne_username = 'DNE1'

        UsersController.add_user(test_username)
        UsersController.add_user(test_username2)

        # Add invalid card to existing user
        self.assertFalse(UsersController.add_credit_card(test_username,
                                                         invalid_card))

        # Add valid card to existing user
        self.assertTrue(UsersController.add_credit_card(test_username,
                                                        valid_card))

        # Add a valid card to a user that already has a card
        self.assertFalse(UsersController.add_credit_card(test_username,
                                                         valid_card))

        # Add valid card that belongs to someone else
        self.assertFalse(UsersController.add_credit_card(test_username2,
                                                         valid_card))

        # Add a valid card to a user that isn't in the database
        self.assertFalse(UsersController.add_credit_card(dne_username,
                                                         valid_card))
        Database.db.clear_db()

    def test_display_balance(self):
        test_username = "Tobias-P_88"
        dne_username = 'DNE1'

        UsersController.add_user(test_username)
        # Make call to display balance method and should return True
        self.assertTrue(UsersController.display_balance(test_username))

        # Try to get balance for user that doesn't exist
        self.assertFalse(UsersController.display_balance(dne_username))

        Database.db.clear_db()

if __name__ == '__main__':
    unittest.main()

import unittest
from minivenmo.user.UsersController import UsersController, Database


class TestUserController(unittest.TestCase):
    def test_add_user(self):
        new_username = "Tobias-P_88"
        invalid_user = "Tobias!@#$%^&*"

        # Add a user and check to see if the name property matches its object
        UsersController.add_user(new_username)
        user = Database.db.lookup_user(new_username)
        self.assertEqual(user.name, new_username)

        # Add invalid username and check for exception
        self.assertRaises(Exception, UsersController.add_user, invalid_user)

        # Add an existing user
        self.assertRaises(Exception, UsersController.add_user, new_username)

    def test_add_credit_card(self):
        valid_card = "4111111111111111"
        invalid_card = "12345678910111213"

        existing_username = "Tobias-P_88"
        new_username = 'test_user'
        dne_username = 'DNE'

        user = Database.db.lookup_user(existing_username)
        UsersController.add_user(new_username)

        # Add invalid card to existing user
        self.assertRaises(Exception, UsersController.add_credit_card,
                          existing_username, invalid_card)

        # Add valid card to existing user
        UsersController.add_credit_card(existing_username, valid_card)
        self.assertEqual(user.card_number, valid_card)

        # Add a valid card to a user that already has a card
        self.assertRaises(Exception, UsersController.add_credit_card,
                          existing_username, valid_card)

        # Add valid card that belongs to someone else
        self.assertRaises(Exception, UsersController.add_credit_card,
                          new_username, valid_card)

        # Add a valid card to a user that isn't in the database
        self.assertRaises(Exception, UsersController.add_credit_card,
                          dne_username, valid_card)

    def test_display_balance(self):
        # existing_username = "Tobias-Perelstein_88"
        dne_username = 'DNE'

        # user = Database.db.lookup_user(existing_username)

        # self.assertIsInstance(user.balance, float)

        # Try to get balance for a user that doesn't exist in the database
        self.assertRaises(Exception, UsersController.display_balance,
                          dne_username)

if __name__ == '__main__':
    Database.init_db()
    unittest.main()

import unittest
from minivenmo import Database
from tests.test_user import TestUserController
from tests.test_transaction import TestTransactionsController

if __name__ == '__main__':
    Database.init_db()
    unittest.main()

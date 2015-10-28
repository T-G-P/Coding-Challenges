import unittest
from minivenmo import Database
from tests.test_user import TestUsersController
from tests.test_transaction import TestTransactionsController
from tests.test_router import TestRouter

if __name__ == '__main__':
    Database.init_db()
    unittest.main()

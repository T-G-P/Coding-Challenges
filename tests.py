import unittest
from tests.test_user import TestUserController, Database

if __name__ == '__main__':
    Database.init_db()
    unittest.main()

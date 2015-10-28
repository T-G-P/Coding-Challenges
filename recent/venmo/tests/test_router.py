import unittest
import os
from minivenmo.MiniVenmo import MiniVenmo


class TestRouter(unittest.TestCase):
    def test_process_args(self):
        # Test for invalid argument lengths and unkown arguments
        app = MiniVenmo()
        bad_args = ['pay', 'user', 'add', 'feed', 'balance', 'foobar']
        good_args = [
            'user Tobias',
            'add Tobias 4111111111111111',
            'user Test',
            'pay Tobias Test $66.60 hello world',
            'balance Tobias',
            'balance Test',
            'feed Tobias',
            'feed Test'
        ]
        for arg in bad_args:
            with self.assertRaises(Exception) as cm:
                app._MiniVenmo__process_args(arg.split())
            exception = cm.exception
            self.assertIn("ERROR:", exception.message)

        for arg in good_args:
            self.assertTrue(app._MiniVenmo__process_args(arg.split()))

    def test_process_file(self):
        app = MiniVenmo()
        good_args = 'test.txt'
        bad_args = 'DNE.txt'
        if not os.path.exists(good_args):
            with open(path_to_file, "w+"):
                pass

        self.assertRaises(IOError, app._MiniVenmo__process_file, bad_args)
        # File may contain bad arguments which are tested in process_args so
        # pass on any Exceptions encountered from process_args
        try:
            self.assertTrue(app._MiniVenmo__process_args(good_args))
        except Exception:
            pass

    def test_usage(self):
        app = MiniVenmo()
        self.assertTrue(app._MiniVenmo__usage())

if __name__ == '__main__':
    unittest.main()

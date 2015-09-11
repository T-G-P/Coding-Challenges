import unittest
from incr_dict import incr_dict


class TestIncrDict(unittest.TestCase):
    def test_bad_input(self):
        # invalid data types entered
        with self.assertRaises(Exception) as cm:
            data = []
            tup = {'a','b'}
            incr_dict(data, tup)

            data = {}
            tup = '5'
            incr_dict(data, tup)

            data = 'a'
            tup = 'a', 'b', 'c'
            incr_dict(data, tup)
        exception = cm.exception
        self.assertEqual(
            exception.message,
            "Invalid data types. Must be dict and tuple.")

        # Empty tuple passed in
        with self.assertRaises(Exception) as cm:
            data = {}
            tup = ()
            incr_dict(data, tup)
        exception = cm.exception
        self.assertEqual(
            exception.message,
            "Invalid tuple, must have at least 1 value")

    def test_valid_input(self):
        data = {}

        # Test case where root is leaf
        self.assertEqual(
            incr_dict(data, tuple('a')),
            {'a': 1}
        )
        # Test case where root is leaf and incremenation
        self.assertEqual(
            incr_dict(data, tuple('a')),
            {'a': 2}
        )

        # Test basic example where old root is no longer leaf
        self.assertEqual(
            incr_dict(data, ('a', 'b', 'c')),
            {'a': {'b': {'c': 1}}}
        )

        # Check to see that leaf node gets incremented
        self.assertEqual(
            incr_dict(data, ('a', 'b', 'c')),
            {'a': {'b': {'c': 2}}}
        )

        # Check to see that a new leaf node gets created
        self.assertEqual(
            incr_dict(data, ('a', 'b', 'f')),
            {'a': {'b': {'c': 2, 'f': 1}}}
        )

        # Check to see that a new intermediate node is created
        # and a leaf node for that new node is created
        self.assertEqual(
            incr_dict(data, ('a', 'r', 'f')),
            {'a': {'r': {'f': 1}, 'b': {'c': 2, 'f': 1}}}
        )

        # Check for a new leaf node to be created at the same level as
        # the intermediate nodes
        self.assertEqual(
            incr_dict(data, ('a', 'z')),
            {'a': {'r': {'f': 1}, 'b': {'c': 2,'f': 1}, 'z': 1}}
        )


        # Test case where unsetting terminal leaf value and setting it
        # to have a dict child
        self.assertEqual(
            incr_dict(data, ('a', 'z', 'h')),
            {'a': {'r': {'f': 1}, 'b': {'c': 2, 'f': 1}, 'z': {'h': 1}}}
        )

        # starting over with a new dict
        self.assertEqual(
            incr_dict(data, ('b', 'c', 'd')),
            {'b': {'c': {'d': 1}}}
        )

        # Testing for large input
        import random
        import string
        data.clear()
        tup = [random.choice(string.lowercase) for i in range(1000)]

        # function returns a dict on success
        self.assertIsInstance(incr_dict(data, tuple(tup)), dict)

if __name__ == '__main__':
    unittest.main()

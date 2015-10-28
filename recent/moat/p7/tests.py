import unittest
import string
import random
from MyHash import MyHash


class TestMyHash(unittest.TestCase):

    def test_set_and_get(self):
        hash_table = MyHash()
        # test basic set and get functionality for strings
        hash_table.set('hello', 'world')
        self.assertEqual(hash_table.get('hello'), 'world')

        # test basic set and get functionality for ints
        hash_table.set(3, 5)
        self.assertEqual(hash_table.get(3), 5)

        # test basic set and get functionality for objects
        class test(object):
            pass

        class test2(object):
            pass

        key = test()
        val = test2()

        hash_table.set(key, val)
        self.assertIsInstance(hash_table.get(key), test2)

        # test for invalid key
        self.assertRaises(KeyError, hash_table.get, 'test')

    def test_delete(self):
        hash_table = MyHash()

        # Test basic deletion
        hash_table.set('hello', 'world')
        length = len(hash_table.values())
        hash_table.delete('hello')
        self.assertLess(len(hash_table.values()), length)

    def test_keys_and_values(self):
        hash_table = MyHash()

        # random character generator for easy test insertion
        def random_val():
            return random.choice(string.lowercase)

        [hash_table.set(random_val(), random_val()) for i in range(8)]
        self.assertEqual(len(hash_table.values()), 8)
        self.assertEqual(len(hash_table.keys()), 8)

    def test_resize(self):
        hash_table = MyHash()

        # test both increasing in size when load factor is met
        original_length = len(hash_table._buckets)
        for i in range(30):
            key = ''.join(random.choice(string.lowercase) for i in range(3))
            val = ''.join(random.choice(string.lowercase) for i in range(3))
            hash_table.set(key, val)

        new_length = len(hash_table._buckets)
        self.assertGreater(new_length, original_length)

        # test decreasing in size when load is too small
        for key in hash_table.keys()[:26]:
            hash_table.delete(key)

        new_length = len(hash_table._buckets)
        self.assertEqual(new_length, original_length)

if __name__ == '__main__':
    unittest.main()

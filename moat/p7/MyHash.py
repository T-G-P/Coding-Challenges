"""
@Author Tobias Perelstein
Design and implemented with influence from the following resources:

http://goodmath.scientopia.org/2013/10/20/basic-data-structures-hash-tables/
http://kells.tj/blog/2015/04/26/pure-python-hashtable.html
https://sites.google.com/site/usfcomputerscience/hash-tables-imp

I implemented this to provide amortized O(1) lookup and insertion time
by focusing heavily on picking the right hash function and allowing
for various table sizes based on a load factor. Once the load factor is
reaches, the table is resized and rehashed and the items get redistributed
The Hash table uses a list of lists for each bucket in order to resolve
collisions by chaining them. The chaining occurs by appending the item class
to the list at the index returned from the hash function.

Load factor and size constants taken from examples and other implementations.
"""


class Item:
    """
    Item class represents the key value pair inserted
    into the dictionary. Abstracted to make things more clear
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return '<Item: (%s => %s) >' % (self.key, self.value)


class MyHash:
    """Main Hash implementation. The class has the min size property
    to initialize the size of the table, the load factor property to
    determine when or not to resize, and the load amount, which is
    calculated during insertion or deletion. The minimum load is used
    to reduce the size of the hash table if it's sparsely populated and
    bigger than the minimum size. The size factor is the factor used
    to resize and rehash all the values in the table.
    """

    _min_size = 8
    _size = _min_size
    _load_factor = .66
    _min_load = .16
    _load_amount = 0
    _size_factor = 4

    def __init__(self):
        self._buckets = [[] for i in range(self._min_size)]

    def get(self, key):
        """Gets the value from the hash based on the key"""

        index = self._hash_djb2(key)
        for item in self._buckets[index]:
            if item.key == key:
                return item.value
        raise KeyError(key)

    def set(self, key, value, item=None):
        """Sets the value based on the key. Used
        internally as well during resize to copy items
        """

        if self._load >= self._load_factor:
            self._resize(len(self._buckets) * self._size_factor)
        if not item:
            if not key:
                raise KeyError(key)
            elif not value:
                raise ValueError(value)
            item = Item(key, value)
        index = self._hash_djb2(item.key)
        self._buckets[index].append(item)

    def delete(self, key):
        """Checks the total bucket usage on call to delete,
        and resizes the table by a factor of 4
        """

        index = self._hash_djb2(key)
        self._buckets[index] = []

        # If the buckets seem under-utilized, resize and rehash
        if 0 < self._load <= self._min_load:
            if len(self._buckets) > self.min_size:
                self._resize(len(self._buckets) / self._size_factor)

    def _resize(self, size):
        """Resizes the hash table either on insertion or deletion.
        Copies over all the old information and calls the set method
        internally to rehash all the items
        """
        old_buckets = self._buckets
        self._buckets = [[] for i in range(size)]
        self._size = size

        # Make sure the old data gets re-indexed into the new store
        for bucket in old_buckets:
            for item in bucket:
                self.set(item.key, item.value, item)

    @property
    def _load(self):
        """Deterimines the overall load amount. Used as a property
        to compare to the maximum load factor of 2/3
        """
        items = [bucket[0] for bucket in self._buckets if len(bucket)]
        try:
            self._load_amount = float(len(items)) / float(len(self._buckets))
        except ZeroDivisionError:
            return 0
        return self._load_amount

    def _hash_djb2(self, key):
        """
        Taken from here https://gist.github.com/SaveTheRbtz/2117117
        I did some research and saw that this hash function has a
        good reputation. This is the python equivalent to the C
        implementation here http://www.cse.yorku.ca/~oz/hash.html
        """
        _hash = 5381
        # in the event an int is passed in for a key
        key = str(key)

        for i in range(0, len(key)):
            _hash = ((_hash << 5) + _hash) + ord(key[i])

        return _hash % self._size

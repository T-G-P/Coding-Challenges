"""
@Author: Tobias Perelstein

Removed call to reduce because it is unecessary. It works great
for getting nested values from a dictionary  but calling reduce while
simultaneously iterating over the letters is a redundant and
more expensive solution (still better than recursive). Also, I was only calling
reduce for one letter at a time, thus defeating the purpose of using it. It's
great for getting nested values of a dictionary, but was an overcomplication
for the purpose of this problem. I also cleaned up the code to only have one return
Got rid of some redundant logic as well.

The implementation of incr_dict below was designed with a large
data set in mind. I initially approached the problem recursively,
but then realized that I would exceed recursion depth in the situation
that the data set is too large. As a result, I chose the iterative approach.

The function iterates over the letters by index and value and
uses the 'setdefault' method of dicts which makes it very easy
to nest a dictionary since the method returns 'self'. I made
use of this method and iteratively nested the dictionaries
until i reached the last letter, in which case I set that to 1

Counts are incremented in the event the order of the tuples
are consistent across multiple calls. If a new letter is
passed in after a value that was terminal perviously,
its data is erased and set to a new dict.

"""

def incr_dict(data, tup):
    if not all([isinstance(data, dict), isinstance(tup, tuple)]):
        raise Exception("Invalid data types. Must be dict and tuple.")
    if not tup:
        raise Exception("Invalid tuple, must have at least 1 value")

    # cast tuple as list for lists flexibility/methods
    letters = list(tup)

    # if the first letter is not in the nested dict, clear it
    if letters[0] not in data:
        data.clear()

    # set curr, prev value to use for looking up nested values
    prev = None
    curr = data

    for index, letter in enumerate(letters):
        # last index
        if index == len(letters)-1:
            try:
                # try to get value at this key
                curr[letters[index]]
            except KeyError:
                # letter doesnt exist, setting it
                curr.setdefault(letter, 1)
            except TypeError:
                # curr is an int at this point
                # (meaning we need to change this into to a dict)
                # can't call get on an int
                # use dict from previous iteration and previous key
                prev[letters[index-1]] = {letter: 1}
            else:
                # accounted for all cases where count needs to be
                # initialized so increment count
                curr[letter] += 1
        else:
            prev = curr
            curr = curr.setdefault(letter, {})

    return data

def main():
    data = {}
    incr_dict(data, ('a', 'b', 'c'))
    print(data)
    incr_dict(data, ('a', 'b', 'c'))
    print(data)
    incr_dict(data, ('a', 'b', 'f'))
    print(data)
    incr_dict(data, ('a', 'r', 'f'))
    print(data)
    incr_dict(data, ('a', 'z'))
    print(data)
    incr_dict(data, ('a', 'z', 'h'))
    print(data)
    incr_dict(data, ('b', 'c', 'd'))
    print(data)

    try:
        incr_dict(data, ())
    except Exception as e:
        print(e.message)

    try:
        incr_dict([], {})
    except Exception as e:
        print(e.message)

if __name__ == '__main__':
    main()

"""
@Author: Tobias Perelstein

The implementation of incr_dict below was designed with a large
data set in mind. I initially approached the problem recursively,
but then realized that I would exceed recursion depth in the situation
that the data set is too large. As a result, I chose the iterative approach.
I made use of 'reduce' which iteratively retreives the values for
the dictionary and returns the value at the key if it exists. If
the key doesn't exist, it's created and set to 1. If, it was the
terminal value from a previous call, then reduce won't work, so
I make use of the previous iterations dictionary and set it to
have a default value of {letter: 1}

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

    # cast tuple as list for lists flexibility/methods
    letters = list(tup)

    # if the first letter is not in the nested dict, clear it
    if letters[0] not in data:
        data.clear()

    # set curr, prev value to use for looking up nested values
    prev = data
    curr = data

    for index, letter in enumerate(letters):
        # last index
        if index == len(letters)-1:
            try:
                # reduces to single value from nested dict.
                # iterates over the letters from each index
                reduce(lambda d, k: d[k], letters[index:], curr)
            except KeyError:
                # letter doesnt exist, setting it
                curr = curr.setdefault(letter, 1)
                return data
            except TypeError:
                # unable to reduce to value
                # letter exists but it's already set to an int
                # set curr dict at previous letter
                prev[letters[-2]] = {letter: 1}
                return data

            # Check to see if the last value
            # is a dictionary or not. If it is
            # then clear it out and set it to 1, otherwise increment
            val = curr.setdefault(letter, {})
            if isinstance(val, dict):
                curr[letter].clear()
                curr[letter] = 1
                return data
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

if __name__ == '__main__':
    main()

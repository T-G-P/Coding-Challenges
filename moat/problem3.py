"""
@Author: Tobias Perelstein
"""





def incr_dict(data, tup):
    letters = list(tup)

    if letters[0] not in data:
        data.clear()

    # set prev value to use for looking up nested values
    prev = data

    for index, letter in enumerate(letters):
        # last index
        if index == len(letters)-1:
            try:
                # reduces to single value from nested dict.
                # iterates over the letters from each index
                reduce(lambda d, k: d[k], letters[index:], data)
            except KeyError:
                # letter doesnt exist, setting it
                data = data.setdefault(letter, 1)
                return data
            except TypeError:
                # unable to reduce to value
                # letter exists but it's already set to an int
                # set data dict at previous letter
                prev[letters[-2]] = {letter: 1}
                return data

            val = data.setdefault(letter, {})
            if isinstance(val, dict):
                data[letter].clear()
                data[letter] = 1
                return data
            data[letter] += 1
        else:
            prev = data
            data = data.setdefault(letter, {})

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

if __name__ == '__main__':
    main()

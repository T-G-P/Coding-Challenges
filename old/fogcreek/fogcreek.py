import re
import os
import argparse

def get_secret_word(infile):
    """
    Loops through file line by line, and substituets all unwanted characters
    that aren't lowercase letters or underscores

    Loops through all characters in line and sets their respective count in a
    dictionary

    Sorts the dictionary by value in reverse order and then returns
    the secret word using the _ as the delimiter.
    """
    character_map = {}
    with open(infile) as f:
        for line in f:
            line = re.sub('[^a-z_]+', '', line)
            for c in line:
                character_map[c] = character_map.get(c,0) + 1

    sorted_string = ''.join(
        sorted(character_map, key=character_map.get, reverse=True)
    )
    return sorted_string.split('_')[0]


def get_args():
    """
    Reads arguments from the command line and returns them
    If the input file is invalid, an exception will be raised
    """

    def is_valid_file(parser, arg):
        """Checks whether the file exists on the filesystem
        Raises an error if it doesnt exist or returns the argument
        if it does
        """

        arg = os.path.abspath(arg)
        if not os.path.exists(arg):
            parser.error("The file %s does not exist!" % arg)
        else:
            return arg

    parser = argparse.ArgumentParser(description='Process file and find the secret word')
    parser.add_argument("-f", "--file",
                        dest="filename",
                        type=lambda x: is_valid_file(parser, x),
                        required=True,
                        metavar="FILE",
                        help="Pass the file for processing with this flag")
    args = parser.parse_args()
    return args


def main():
    args = get_args()
    print(get_secret_word(args.filename))


if __name__ == '__main__':
    main()

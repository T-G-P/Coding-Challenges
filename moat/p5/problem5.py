import argparse


def main():
    parser = argparse.ArgumentParser(description='P5')
    parser.add_argument('filename', nargs='?')
    args = parser.parse_args()

    if args.filename:
        result = process_file(args.filename)

        for k, v in result.items():
            print('%s => %d\n' % (k, v))


def process_file(file_name):
    """
    Won't be good for large files, need to implement
    either with generator or a database
    """
    valid_chars = "[ \t{}[]\n]+"
    result = {c: 0 for c in valid_chars}
    try:
        with open(file_name) as f:
            for line in f:
                for c in line:
                    if c in valid_chars:
                        result[c] += 1
    except IOError:
        raise
    return result

if __name__ == '__main__':
    main()

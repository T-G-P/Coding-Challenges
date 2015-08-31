import argparse
from json import dumps


def output(dictionary):
    print(dumps(dictionary, sort_keys=True))

def generate_item_sets(filename):
    with open(filename) as items_file:
        # process file line by line, strip new lines, tokenize on commas
        # cast each line as a set for flexibile and fast operations
        print("\nProcessing %s ..." % filename)
        item_sets = [
            set(item.rstrip('\n').split(','))
            for item in items_file
        ]
        print("Done processing %s\n" % filename)

    return item_sets

def get_word_frequency(files):
    try:
        query_sets, record_sets = tuple(map(generate_item_sets, files))
    except IOError as e:
        print(str(e))
        return

    # check that query is a subset, take difference and build result
    for query_set in query_sets:
        res = {}
        for record_set in record_sets:
            if query_set.issubset(record_set):
                difference = record_set.difference(query_set)
                for word in difference:
                    if word not in res:
                        res[word] = 1
                    else:
                        res[word] += 1

        output(res)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get the Word Frequency')
    parser.add_argument("queries", help="The queries text file")
    parser.add_argument("records", help="The records text file")
    args = parser.parse_args()

    get_word_frequency([args.queries, args.records])

from json import dumps


def output(dictionary):
    print(dumps(dictionary, sort_keys=True))


def get_word_frequency():

    with open('queries.txt') as queries_file:
        # make query set sa generator as it's only needed once
        query_sets = (
            set(query.rstrip('\n').split(','))
            for query in queries_file
        )
        with open('records.txt') as records_file:
            # make record_sets a list as it's needed for every query
            record_sets = [
                set(record.rstrip('\n').split(','))
                for record in records_file
            ]
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
    get_word_frequency()

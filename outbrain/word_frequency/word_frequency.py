from json import dumps

records = open('records.txt')
queries = open('queries.txt')


def output(dictionary):
    print(dumps(dictionary, sort_keys=True))


def get_word_frequency():
    # with open('queries.txt') as queries:
    for query in queries:
        query_set = set(query.rstrip('\n').split(','))
        res = {}
        check_query(query_set, res)


def check_query(query_set, res):
    # with open('records.txt') as records:
    for record in records:
        record_set = set(record.rstrip('\n').split(','))
        if query_set.issubset(record_set):
            difference = record_set.difference(query_set)
            for word in difference:
                if word not in res:
                    res[word] = 1
                else:
                    res[word] += 1

    output(res)
    records.seek(0)

get_word_frequency()

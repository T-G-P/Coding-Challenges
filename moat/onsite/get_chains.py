requests = [
    {
        'url': 'A',
        'data': ['B', 'C']
    },
    {
        'url': 'B',
        'data': ['D', 'E']
    },
    {
        'url': 'D',
        'data': ['G', 'H']
    }
]

def get_chains(requests, url):
    requests_map = {}
    result = []
    for item in requests:
        for letter in item['data']:
            requests_map[letter] = item['url']

    parent = requests_map.get(url)
    while parent:
        result.append(parent)
        parent = requests_map.get(parent)

    return tuple(result[::-1])

if __name__ == '__main__':
    print(get_chains(requests, 'E'))
    print(get_chains(requests, 'D'))
    print(get_chains(requests, 'G'))
    print(get_chains(requests, 'H'))
    print(get_chains(requests, 'B'))
    print(get_chains(requests, 'C'))

In person question #3
=====================

Given a requests object like this:

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
....
]

Find all parent chains for a given node.
Ex:
get_chains(requests, 'B')
returns ('A')

get_chains(requests, 'D')
returns ('A', 'B')

get_chains(requests, 'G')
returns ('A', 'B', 'D')

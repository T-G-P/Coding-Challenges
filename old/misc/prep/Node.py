import random


class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


def build_list():
    ll = Node(5, None)
    curr = ll
    for i in range(5):
        node = Node(random.randint(0, 9), None)
        curr.next = node
        curr = curr.next
    return ll


def print_list(node):
    curr = node
    while curr:
        print(curr.data)
        curr = curr.next
    print('\n')


def reverse_list(node):
    prev = None
    curr = node

    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev

ll = build_list()
print_list(ll)
new_ll = reverse_list(ll)
print_list(new_ll)

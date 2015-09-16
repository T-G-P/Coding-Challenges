import argparse


def build_tree(filename):
    """
    Build data structure out of tree for easy processing.
    Each row in the tree is a list within a list
    """
    with open(filename) as f:
        tree = [list(map(int, line.split())) for line in f]
    return tree


def max_sum(tree):
    """
    The algorithm used here to find the maximum sum
    finds all possible routes by summing all possible
    cases at each row and then taking the max of the final
    sum. If at the first or last node, the immediate adjacent
    node from the previous sum is added. If in between, the max
    of the nodes adjacent to the inner child is added to the
    child so that the maximum sum at this iteration is found
    This way, if there is a very large number found in one of
    the rows, this path will counted.
    """
    sums = tree[0]
    for row in tree[1:]:
        next_sums = []
        for i in range(len(row)):
            if i == 0:
                next_sums.append(row[i]+sums[i])
            elif i == len(row) - 1:
                next_sums.append(row[i]+sums[i-1])
            else:
                next_sums.append(row[i]+max(sums[i-1], sums[i]))
        sums = next_sums

    return max(sums)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Triangle max sum')
    parser.add_argument("triangle", help="The triangle text file")
    args = parser.parse_args()

    tree = build_tree(args.triangle)
    print(max_sum(tree))

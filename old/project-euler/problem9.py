'''


A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

'''
def pythag_triplet(a,b,c):
    if a**2+b**2==c**2:
        return True
    return False


def calculate_triplet():
    for c in xrange(333,707):
        for b in xrange(0,c,5):
            for a in xrange(0,b,5):
                if pythag_triplet(a,b,c) and a+b+c==1000:
                    print a,b,c
                    return a*b*c

print calculate_triplet()

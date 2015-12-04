'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''
import sys

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True

    for i in xrange(3,int(n**.5)+1):
        if n % i == 0:
            return False
    return True

def nth_prime(n):
    num_primes = 1
    for k in xrange(1,sys.maxint,2):
        if is_prime(k):
            #print k
            num_primes += 1
        if num_primes == n:
            return k

print nth_prime(10001)


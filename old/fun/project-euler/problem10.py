'''The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.'''

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True

    for i in xrange(2,int(n**.5)+1):
        if n % i == 0:
            return False
    return True

def sum_primes(n):
    sum_primes = 2
    for i in xrange(1,n,2):
        if is_prime(i):
            ret += i
    return ret

print sum_primes(2000000)

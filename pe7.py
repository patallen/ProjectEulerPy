# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.

# What is the 10 001st prime number?
from math import sqrt


def nth_prime_quick(n=10001):
    next_ = 3
    known_primes = [2]
    while True:
        is_prime = True
        squarert = sqrt(next_)
        for x in known_primes:
            if x > squarert:
                if is_prime:
                    known_primes.append(next_)
                    if len(known_primes) == n:
                        return next_
                break
            if next_ % x == 0:
                is_prime = False
        next_ += 2


def nth_prime_slow(n=10001):
    next_ = 3
    known_primes = [2]
    while True:
        squarert = sqrt(next_)
        if all(next_ % x != 0 for x in known_primes if x <= squarert):
            known_primes.append(next_)
            if len(known_primes) == n:
                return next_
        next_ += 2


if __name__ == '__main__':
    import timeit
    iterations = 5

    fast = timeit.timeit(
        'nth_prime_quick()',
        number=iterations,
        setup='from __main__ import nth_prime_quick'
    )/iterations
    print "Avg Fast: %s" % round(fast, 3)

    slow = timeit.timeit(
        'nth_prime_slow()',
        number=iterations,
        setup='from __main__ import nth_prime_slow'
    )/iterations
    print "Avg Slow: %s" % round(slow, 3)

    print "Fast is %sx times faster." % str(round(slow/fast, 3))

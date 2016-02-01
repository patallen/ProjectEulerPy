# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
from math import sqrt, floor


def largest_prime(limit):
    plimit = floor(sqrt(limit))
    next_ = 3
    last_factor = next_
    primes = [1, 2]
    while next_ <= plimit:
        if all([next_ % x != 0 for x in primes[1:]]):
            primes.append(next_)
            if limit % next_ is 0:
                last_factor = next_
        next_ += 2
    return last_factor


print largest_prime(600851475143)

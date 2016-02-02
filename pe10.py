# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.


def prime_sieve(limit=10000):
    primes = []
    sieve = [True for x in xrange(limit+1)]
    sieve[0] = False
    for num, b in enumerate(sieve, 1):
        if b:
            primes.append(num)
            for x in range(num+num, limit+2, num):
                sieve[x-1] = False
    return primes
print sum(prime_sieve(2000000))

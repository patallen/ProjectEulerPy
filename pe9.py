
def get_pythagorean_triplet(tsum=1000):
    for x in xrange(1, tsum+1):
        for y in xrange(1, tsum+1):
            i = tsum-x-y
            if (x*x)+(y*y) == i*i:
                prod = 1
                for x in (x, y, i):
                    prod *= x
                return prod

print get_pythagorean_triplet()

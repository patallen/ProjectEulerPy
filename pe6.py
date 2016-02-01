# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.


def square_of_sum(limit):
    s = sum(xrange(1, limit+1))
    return s * s


def sum_of_squares(limit):
    return sum([x*x for x in xrange(1, limit+1)])

print square_of_sum(100) - sum_of_squares(100)

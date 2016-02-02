# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 21000?


def sum_of_pow_digits(n=2, exp=1000):
    result = n
    for x in xrange(exp-1):
        result *= n
    return sum(int(x) for x in str(result))

print sum_of_pow_digits()

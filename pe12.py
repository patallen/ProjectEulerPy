import math


# Triangle Number Generator
def itriangle():
    cnt, cur = 1, 0
    while True:
        cnt, cur = cnt+1, cur+cnt
        yield cur


def factors_of(num):
    sqrt = int(math.floor(math.sqrt(x)))
    factors = []
    for y in range(1, sqrt):
        if x % y == 0:
            factors.append(y)
            factors.append(x/y)
    return factors

for x in itriangle():
    factors = factors_of(x)
    if len(factors) >= 500:
        print x
        break

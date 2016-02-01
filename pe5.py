# 2520 is the smallest number that can be divided by each
# of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly
# divisible by all of the numbers from 1 to 20?


def divisible_by_all(rangeof=20):
    nums = range(2, rangeof+1)
    for i, x in enumerate(reversed(nums)):
        nums = [y for y in nums if x % y != 0 or y == x]

    next_ = rangeof * 2
    while True:
        if all([next_ % x == 0 for x in nums]):
            return next_
        next_ += rangeof

def sum_squares(target):
    total = 0
    for x in range(0, target + 1):
        total += x**2
    print(total)
    return total


def sum_squared(target):
    total = (target * (target + 1))/2
    return total ** 2

print(sum_squared(100) - sum_squares(100))
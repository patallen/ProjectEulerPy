def divisible_by(num, list_):
    is_divisible = False
    for n in list_:
        if num % n == 0:
            is_divisible = True
            break
    return is_divisible

divisibles = []
for number in range(1000):
    if divisible_by(number, [3, 5]):
        divisibles.append(number)

print sum(divisibles)

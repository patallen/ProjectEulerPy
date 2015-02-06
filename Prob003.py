def is_prime(n):
    xx = 2
    while xx <= n/2:
        if n % xx == 0:
            return False
        xx += 1
    return True

factor_array = []
the_number = 600851475143
y = the_number
x = 2.0
while x < y:
    if the_number % x == 0:
        y /= x
        if is_prime(x):
            factor_array.append(x)
        if is_prime(y):
            factor_array.append(y)
    x += 1

print(max(factor_array))


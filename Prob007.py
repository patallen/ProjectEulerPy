def is_prime(n):
    x = 2
    while x <= n/2:
        if n % x == 0:
            return False
        x += 1
    return True

prime_array = []
curr_num = 2
while len(prime_array) <= 10001:
    if is_prime(curr_num):
        prime_array.append(curr_num)
    print(prime_array[len(prime_array)-1])
    if curr_num > 2:
        curr_num += 2
    else:
        curr_num += 1

print(prime_array[10000])
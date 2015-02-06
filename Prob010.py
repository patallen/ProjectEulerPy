def primes_list(target):
    arr = [True] * target
    arr[0] = arr[1] = False
    prime_array = []

    for idx, val in enumerate(arr):
        if val is True:
            temp = idx
            for x in range(temp+temp, target, temp):
                arr[x] = False

    for idx, val in enumerate(arr):
        if val:
            prime_array.append(idx)

    print(sum(prime_array))

primes_list(2000000)
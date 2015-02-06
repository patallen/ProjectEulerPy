x = 1
z = 1
temp = 0
total = 0

while z < 4000000:
    temp = x
    x = z
    z += temp

    if z % 2 == 0:
        total += z

print(total)
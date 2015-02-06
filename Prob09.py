the_sum = 1000

found = False
a = 0
b = 0

for a in range(a, sum/3, 1):
    for b in range(a + 1, sum/2, 1):
        c = the_sum - a - b
        if a*a + b*b == c*c:
            print(a, b, c, a*b*c)
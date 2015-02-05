from fractions import gcd

x = 20
curr_lcm = x

while x > 1:
    curr_lcm = curr_lcm * (x-1) / gcd(curr_lcm, x-1)
    x -= 1

print(curr_lcm)


# Triangle Number Generator
def itriangle():
    cnt, cur = 1, 0
    while True:
        cnt, cur = cnt+1, cur+cnt
        yield cur

for x in itriangle():
    if x <= 10:
        print x
    else:
        break



def ifib(limit=None):
    count, prev, next_ = 1, 0, 1
    yield next_
    while True:
        yield next_ + prev
        if limit and count > limit:
            break
        prev, next_ = next_, prev+next_
        count += 1


def digits(num):
    return len(str(num))


def fib_digits_index(digs):
    for idx, num in enumerate(ifib(), 1):
        if digits(num) == digs:
            return idx

print fib_digits_index(1000)

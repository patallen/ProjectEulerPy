import csv


def name_score(name="Patrick"):
    scores = {l: s for s, l in enumerate(" abcdefghijklmnopqrstuvwxyz")}
    return sum([scores.get(x) for x in name.lower()])

with open("names.txt") as f:
    names = list(csv.reader(f, delimiter=","))[0]

print sum(map(lambda (y, x): name_score(x)*y, enumerate(sorted(names), 1)))

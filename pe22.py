
def name_score(name="Patrick"):
    scores = {l: s for s, l in enumerate(" abcdefghijklmnopqrstuvwxyz")}
    return sum([scores.get(x) for x in name.lower()])

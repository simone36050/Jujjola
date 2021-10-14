# n-cases verson of dicotomic search


def length(min: int, max: int):
    if abs(min) + abs(max) == abs(min + max):
        # same sign
        return abs(max - min) + 1
    else:
        # opposite sign
        return abs(min) + abs(max) + 1

def groups(amount: int, bins: int):
    res = []

    if amount < bins:
        # add 1 by 1
        for i in range(amount):
            res.append([i, i])
        # fill
        for _ in range(bins - amount):
            res.append([amount - 1, amount - 1])
    else:
        for i in range(bins):
            res.append([
                i * amount // bins,                 # start
                (i + 1) * amount // bins - 1        # end
            ])
    
    return res

def intervals(min: int, max: int, bins: int):
    l = length(min, max)
    gs = groups(l, bins)
    for g in gs:
        g[0] += min
        g[1] += min
    return gs

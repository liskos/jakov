def f(x, y, z, w):
    return ((not(y and (x != z)) or w) and (not z or y))


import itertools


for a in itertools.product([0, 1], repeat=3):
    table = [(0, 0, a[1], a[2]), (0, a[0], 0, 0), (1, a[0], a[1], 1)]
    for p in itertools.permutations("xyzw"):
        if [int(f(**dict(zip(p, t)))) for t in table] == [0, 0, 0]:
            print("".join(p))
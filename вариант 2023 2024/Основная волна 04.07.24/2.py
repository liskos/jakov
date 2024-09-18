def f(x, y, z, w):
    return (not z or not(not y or x)) or w


import itertools


for a in itertools.product([0, 1], repeat=16):
    table = [(0, 1, a[0], a[1]), (a[2], a[3], 0, 0), (a[4], 0, 1, a[5])]
    for p in itertools.permutations("xyzw"):
        if [int(f(**dict(zip(p, t)))) for t in table] == [0, 0, 0]:
            print("".join(p))




def f(x, y, z, w):
    return (x and not y) or (y == z) or not w


import itertools


for a in itertools.product([0, 1], repeat=3):
    table = [(a[1], a[2], 0, 0), (1, 0, a[1], 0), (1, 0, 1, a[1])]
    for p in itertools.permutations("xyzw"):
        if [int(f(**dict(zip(p, t)))) for t in table] == [0, 0, 0]:
            print("".join(p))




def f(x, y, z, w):
    return (x == (not y or (z or x))) and w


import itertools

for a in itertools.product({0, 1}, repeat=7):
    table = [(1, 0, 1, a[0]), (0, a[1], a[2], 0), (1,0, a[3], a[4])]
    for p in itertools.permutations("xyzw"):
        if len(set(table)) == 3 and [f(**dict(zip(p, t))) for t in table] == [1, 1, 1]:
            print("".join(p))

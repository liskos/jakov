import itertools

def f(x, y, z, w):
    return not(x == (w and not z)) and (y == (x and not w))


for a in itertools.product([0, 1], repeat=6):
    table = [(a[0], a[1], 0, a[2]), (a[3], 0, a[4], 0), (0, a[5], 1, 0)]
    for p in itertools.permutations("xyzw"):
        if len(set(table)) == 3 and [f(**dict(zip(p, t))) for t in table] == [1, 1, 1]:
            print("".join(p))
def f(x, y, z, w):
    return (not y or(w == z))or not (not x or z)


import itertools

for a in itertools.product({0, 1}, repeat=7):
    table = [(a[0], a[1], 0, 0), (1, a[2], a[3], a[4]), (0, a[5], a[6], 0)]
    for p in itertools.permutations("xyzw"):
        if len(set(table)) == 3 and [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]:
            print("".join(p))

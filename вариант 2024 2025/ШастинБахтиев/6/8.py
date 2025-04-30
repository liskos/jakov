import itertools
r = [0]*21
for a in itertools.product([0, 1],repeat=20):
    c = a.count(0)
    r[c] += 1
print(r)
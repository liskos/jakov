a = {216}
for i in range(7):
    b = set()
    for x in a:
        b.add(x-5)
        b.add(x*-2)
    a = b.copy()
zv = set()
for n in set(a):
    if n > 0:
        zv.add(n)

print(len(zv),zv)
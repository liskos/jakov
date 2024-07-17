a = {91}
for i in range(11):
    b = set()
    for x in a:
        b.add(x-2)
        b.add(x*-3)
    a = b.copy()
zv = set()
for n in set(a):
    if n < 0:
        zv.add(n)

print(len(zv),zv)
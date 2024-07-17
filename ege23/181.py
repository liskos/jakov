a = {113}
for i in range(17):
    b = set()
    for x in a:
        if x >= 1:
            b.add(x - 1)
        if x >= 2:
            b.add(x - 2)
        if x >= 0:
            b.add(int(x ** 0.5))
    a = b.copy()
print(len(set(a)))



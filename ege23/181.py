a = {113}
for i in range(17):
    b = set()
    for x in a:
        b.add(x - 1)
        b.add(x - 2)
        if x >= 0 and int(x**0.5)**2==x:
            b.add(int(x ** 0.5))
    a = b.copy()
print(len(set(a)))



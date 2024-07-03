a = [5]
for i in range(1,1000):
    b = []
    for x in a:
        b.append(x+2)
        b.append(x+5)
    a = b.copy()
    for z in set(a):
        if a.count(z) == 34:
            print(z)

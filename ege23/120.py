a = [1]
for i in range(1,1000):
    b = []
    for x in a:
        b.append(x+1)
        b.append(x+5)
        b.append(x*3)
    a.extend(b)
for z in set(a):
    if a.count(z) == 175:
        print(z)

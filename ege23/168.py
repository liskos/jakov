a = [1]
for i in range(10):
    b = []
    for x in a:
        b.append(x+4)
        b.append(x+7)
        b.append(x//2)
    a = b.copy()
print(a.count(1))
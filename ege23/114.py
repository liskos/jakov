a = [1]
for i in range(1,6):
    b = []
    for x in a:
        b.append(x+1)
        b.append(x+2)
        b.append(x*2)
    a = b.copy()
    if 28 in a:
        print(i)
print(a.count(28))

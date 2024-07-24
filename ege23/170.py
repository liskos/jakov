a = [[2, 3]]
for i in range(5):
    b = []
    for x in a:
        b.append(sorted([x[0] + 3, x[1]]))
        b.append(sorted([x[0] * 4, x[1]]))
        b.append(sorted([x[0], x[1] + 5]))
        b.append(sorted([x[0], x[1] * 2]))
    a = b.copy()
c = []
for x in a:
    if x[1] % x[0] != 0:
        c.append(str(x[0])+"_"+str(x[1]))
print(len(set(c)))

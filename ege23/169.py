a = [[1]]
for i in range(9):
    b = []
    for g in a:
        b.append(g+[g[-1]+3])
        b.append(g+[g[-1]-1])
    a = b.copy()
k = 0
for x in a:
    if x[0] == x[-2] and x[1] == x[-1]:
        k+=1
print(k)
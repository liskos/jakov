def f(filename):
    file = open(filename)
    n = int(file.readline())
    a = [list(map(str,file.readline().split())) for _ in range(n)]
    a = [[int(a[x][0]),int(a[x][1]),(a[x][2])] for x in range(len(a))]
    print(a[:30])

    a = [[int(a[x][0]),int(a[x][1]),(a[x][2])] for x in range(len(a)) if a[x][2] == "#00FF00" or a[x][2] == "#0000FF"]

    print(a[:30])
    a = sorted(a, key=lambda x:(x[0],x[1]))
    print(a)
    k = 0
    b = []
    for i in range(len(a)-3):
        if a[i+3][2] == "#00FF00" and a[i+2][2] != a[i+3][2] and a[i+1][2] != a[i+3][2] and a[i+4][2] != a[i+3][2] and a[i+6][2] != a[i+3][2] and a[i+4][2] != a[i+3][2]:
            k+=1
            b.append(a[i][0])

    return k,max(b)

print(f("87test.txt"))
print(f("26data/26-87.txt"))
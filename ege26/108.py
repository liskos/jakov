def f(filename):
    file = open(filename)
    n,m = map(int,file.readline().split())
    a = [list(map(int,file.readline().split())) for _ in range(n)]
    a = [[a[x][0],a[x][1],a[x][2],max(a[x][3],a[x][-1])]for x in range(len(a))]
    a = sorted(a,key=lambda x:(-x[0],-(x[1]+x[2]+x[3])))
    print(a)
    k = 0
    b = []
    v = []
    for i in range(len(a)):
        if k < m:
            k += 1
            b.append(a[i][1]+a[i][2]+a[i][3])
    k1 = 0
    for x in range(len(a)):
        if k1 < m and a[x][0] == 0:
            v.append(a[x][1]+a[x][2]+a[x][3])

    return min(b),max(v)
    # print(a)


print(f("26data/26-108.txt"))
print(f("108test.txt"))
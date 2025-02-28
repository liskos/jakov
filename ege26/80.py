def f(filename):
    file = open(filename)
    n = int(file.readline())
    a = [list(map(int,file.readline().split())) for _ in range(n)]
    a = sorted(a,key=lambda x:(x[0],x[1]))
    k = 0
    s = 0
    print(a)
    b = []
    a.append([999912,999912])
    for i in range(len(a)-1):
        if a[i][1] - a[i+1][1] <= -3 and a[i][0] == a[i+1][0]:
            k += (a[i+1][1] - a[i][1]) // 3
            s += (a[i+1][1] - a[i][1]) // 3
        if a[i][0] != a[i+1][0]:
            b.append([a[i][0],s])
    b = sorted(b, key=lambda x: -x[1])
    print(b)
    return k,b[0][0]



print(f("80test.txt"))
print(f("26data/26-80.txt"))
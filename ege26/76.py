def f(filename):
    file = open(filename)
    l,n = map(int,file.readline().split())
    a = [list(map(int,file.readline().split())) for _ in range(n)]
    a = sorted(a,key=lambda x:x[1])
    print(a)
    k = 0
    b = []
    for i in range(len(a)-1):
        if a[i][1] != a[i+1][0]:
            k += a[i+1][0] - a[i][1]
            b.append(a[i+1][0]-a[i][1])

    return k,max(b)


print(f("76test.txt"))
print(f("26data/26-76.txt"))
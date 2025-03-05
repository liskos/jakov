def f(filename):
    file = open(filename)
    n = int(file.readline())
    a = [list(map(int,file.readline().split())) for _ in range(n)]
    a = sorted(a,key=lambda x:(x[0],-x[1]))
    print(a)
    k = 0
    v = 0
    b  = []
    for i in range(n-1):
        if a[i][1]-a[i+1][1] <= 10 and a[i][0] == a[i+1][0]:
            k += a[i][1] - a[i+1][1]
            v = a[i][0]
        elif a[i][0] != a[i+1][0]:
            b.append([k+1,v])

    b = max(b,key=lambda x:(x[1],x[0]))
    return b



print(*f("110test.txt"))
print(f("26data/26-110.txt"))
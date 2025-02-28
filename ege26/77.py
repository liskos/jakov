def f(filename):
    file = open(filename)
    n = int(file.readline())
    a = [list(map(int,file.readline().split())) for _ in range(n)]
    a = sorted(a,key=lambda x:(x[0],x[1]))
    a.append([999999,999])
    print(a)
    k = 8
    b = []
    for i in range(len(a)):
        if a[i][1] == a[i-1][1] and a[i][0] == a[i-1][0]:
            None
        elif a[i][0] == a[i-1][0] or i == 0:
            k -= 1
            print(k,a[i])
        else:
            b.append([a[i-1][0],k])
            k = 8
            k-=1
    print(b)
    s = sum([b[x][1] for x in range(len(b))])
    b = sorted(b,key=lambda x:-x[1])
    return s,b[0][0]

print(f("77test.txt"))
print(f("26data/26-77.txt"))
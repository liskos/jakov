def f(filename):
    file = open(filename)
    n,s = map(int,file.readline().split())
    a = [list(map(int,file.readline().split())) for _ in range(n)]
    a = sorted([[x[0],x[1]+x[2]+x[3],x[4]] for x in a],key=lambda x:(-x[1],-x[-1]))
    k = 0
    b = []
    d = []
    x = [x[1] for x in a]
    print(a)
    print(x)
    for i in range(n):
        if x.count(a[i][1]) > 1 and a[0] != a[i]:
            b.append([a[i][0],a[i][1],a[i][2]])
            break
        else:
            k += 1
            d.append(a[i][0])
    b = sorted(b,key=lambda x:(-x[2],x[0]))
    print(b)
    return d[-1],k


print(f("151test.txt"))
print(f("26data/26-151.txt"))












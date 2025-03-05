def f(filename):
    file = open(filename)
    n,m = map(int,file.readline().split())
    a = [list(map(int,file.readline().split())) for _ in range(n)]
    a = sorted(a,key=lambda x:x[0])
    k = 0
    b = []
    pr = 0
    for i in range(n):
        if i > 0 and a[i][0] != a[i-1][0]:
            b.append([a[i-1][0],k,pr])
            pr = 0
            k = 0
        pr += 1
        k += a[i][1]
    b.append([a[-1][0],k,pr])
    b = [[x[0],x[1],x[2]] for x in b if x == min(b) or x == max(b)]
    print(a)
    print(b)
    return sum(x[0] * x[1] for x in b),sum(x[2]-x[1] for x in b)


print(f("136test.txt"))
print(f("26data/26-136.txt"))
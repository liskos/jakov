def f(filename):
    file = open(filename)
    n = int(file.readline())
    a = [list(map(int,file.readline().split())) for _ in range(n)]
    b = [[a[x][0],sum(a[x][1:])//4] for x in range(len(a)) if a[x].count(2) == 0]
    k = int(len(a)*0.25)
    d = [[a[x][0],a[x][1:]] for x in range(len(a)) if a[x].count(2) == 3]
    d = sorted(d,key=lambda x: x[0])
    print(d)
    print(b)
    b = sorted(b,key=lambda x: -x[1])
    b = b[:k+1]
    return b[-1][0],d[0][0]


print(f("154test.txt"))
print(f("26data/26-154.txt"))
def f(filename):
    file = open(filename)
    s,n = map(int,file.readline().split())
    a = [list(map(str,file.readline().split())) for _ in range(n)]
    print(a)
    print(n,s)
    k = 0
    print(max(x[0] for x in a if int(x[0]) <= s))
    for i in range(len(a)):
        while s != 0 or len(a) != 0:
            d = max(x for x in a if int(x[0]) <= s)
            s -= int(d[0])
            a.remove(d)
        k += 1
        s = 5000

    return k
print(f("1.txt"))


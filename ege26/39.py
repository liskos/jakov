def f(filename):
    file = open(filename)
    n,m = map(int,file.readline().split())
    a = [int(file.readline()) for _ in range(n)]
    x = [x for x in a if 180 <= x <= 200]
    a = [b for b in a if x.count(b) == 0]
    a = sorted(a)
    b = []
    k = 0
    for d in a:
        if k + d <= m-sum(x):
            b.append(d)
            k += d
    b.sort(reverse=True)
    print(k)
    print(len(x)+len(b),sum(b)+sum(x))



print(f("39test.txt"))
print(f("26data/26-39"))
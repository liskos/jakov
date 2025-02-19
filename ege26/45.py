def f(filename):
    file = open(filename)
    n = int(file.readline())
    a = [int(file.readline()) for _ in range(n)]
    b = [x for x in a if x % 2 != 0]
    d = [x for x in a if x % 2 == 0]
    print(b,d)
    r = []
    for x in range(len(d)-1):
        if (d[x] + d[x+1]) % 2 == 0 and a.count((d[x]+d[x+1])//2):
            r.append((d[x]+d[x+1])//2)
    for x in range(len(b)-1):
        if (b[x] + b[x+1]) % 2 == 0 and a.count((b[x]+b[x+1])//2):
            r.append((b[x]+b[x+1])//2)
    return len(r),max(r)



print(f("45test.txt"))
print(f("26data/26-45.txt"))
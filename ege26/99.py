def f(filename):
    file = open(filename)
    n,m = map(int,file.readline().split())
    a = [int(file.readline()) for _ in range(n)]
    a = sorted(a)
    a.append(2500)
    k = 0
    b = []
    d = 0
    for i in range(len(a)):
        if d + a[i] <= m:
            d += a[i]
            k += 1
        elif d + a[-1] <= m:
            d += a[-1]
            k += 1
            a.pop(-1)
        else:
            b.append([d,k])
            k = 0
            d = 0
    print(b)
    return len(b),b[-2][0]



print(f("99test.txt"))
print(f("26data/26-99.txt"))


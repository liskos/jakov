def f(filename):
    file = open(filename)
    n = int(file.readline())
    k = int(file.readline())
    m = int(file.readline())
    a = [int(file.readline()) for _ in range(n)]
    a = sorted(a,reverse=True)
    xd = [m] * k
    print(xd)
    print(a)
    b = []
    otv1 = 0
    for i in range(k):
        while len(a) != 0 and xd[i] >= min(a):
            if xd[i] - max(a) >= 0:
                xd[i] -= max(a)
                a.remove(max(a))

            if xd[i] - min(a) >= 0:
                xd[i] -= min(a)
                a.remove(min(a))
            otv1 += 1
        if i < len(xd):
            b.append(xd[i])

    print(xd)
    return otv1



print(f("138test.txt"))
print(f("26data/26-138.txt"))
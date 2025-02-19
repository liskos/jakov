def f(filename):
    file = open(filename)
    n = int(file.readline())
    a = [int(file.readline()) for _ in range(n)]
    k = 0
    kol = 0
    a = sorted(a,reverse=True)
    print(a)
    for x in a:
        if max(a) + min(a) == 100:
            kol += 1
            a.remove(max(a)),a.remove(min(a))
    return kol
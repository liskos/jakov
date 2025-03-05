def f(filename):
    file = open(filename)
    n = int(file.readline())
    a = [int(file.readline()) for _ in range(n)]
    a = sorted(a,reverse=True)
    v = []
    while a:
        v.append(a[0])
        a.pop(0)
        a = [x for x in a if x <= v[-1] - 3]
    return len(v),v[-1]




print(f("89test.txt"))

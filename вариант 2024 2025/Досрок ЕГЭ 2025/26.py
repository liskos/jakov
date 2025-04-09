def f(filename,k):
    file = open(filename)
    n = int(file.readline())
    a = [int(file.readline()) for _ in range(n)]
    a = sorted(a,reverse=True)
    v = []
    while a:
        v.append(a[0]) # матрёшки
        a.pop(0)
        a = [x for x in a if x <= v[-1] - k]
    return len(v),v[-1]

print(*f("26_21424.txt",9))
def f(filename):
    file = open(filename)
    n, m = map(int, file.readline().split())
    a = [list(map(int, file.readline().split())) for _ in range(n)]

    for i in range(len(a)):
        if len(a[i]) == 4:
            a[i] = [a[i][0], a[i][1], a[i][2], a[i][3]]
        else:
            a[i] = [a[i][0], a[i][1], a[i][2], max(a[i][3], a[i][4])]

    a = sorted(a, key=lambda x: (-x[0], -(x[1] + x[2] + x[3])))

    b = []
    v = []
    k = 0
    k1 = 0

    for i in range(n):
        total = a[i][1] + a[i][2] + a[i][3]
        if k < m:
            b.append(total)
            k += 1
        if a[i][0] == 0 and k1 < m:
            v.append(total)
            k1 += 1

    return min(b), min(v)


print(f("26data/26-108.txt"))
print(f("108test.txt"))

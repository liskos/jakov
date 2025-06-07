def f(filename):
    file = open(filename)
    n = int(file.readline())
    a = [int(file.readline()) for _ in range(n)]
    a.sort()
    otv2 = a.copy()
    b = []
    while a:
        d = min([x for x in a if x - a[0] <= 10])
        print(d)
        b.append(d)
        a = [x for x in a if b[-1] + 10 <= x]

    return len(b),max([x for x in otv2 if b[1] - x >= 10])




print(f("26test.txt"))
print(f("files/26_2__6gp6f.txt"))
def f(filename):
    file = open(filename)
    n,k = map(int,file.readline().split())
    a = [list(map(int, file.readline().split())) for _ in range(n)]  # Считываем n строк и преобразуем в список списков
    print(a)
    tr = []
    tr2 = []
    # for i in range(len(a)):
    #     tr.append(a[i][1]//a[i][0])
    # tr = sorted(tr)
    # for i in range(len(a)):
    #     if a[i][1] // a[i][0] == min(tr):
    #         tr2.append(a[i][1])
    #         k -= 1
    # tr = [x for x in tr if x != min(tr)]
    # for g in range(len(a)):
    #     if k != 0 and a[g][1] // a[g][0] == min(tr):
    #         tr2.append(a[g][1])
    #         k -= 1
    mi = set()
    for x in range(len(a)):
        mi.add(a[x][1] // a[x][0])
    x = [[a[x][0],min(mi)] for x in range(len(a)) if a[x][1] // a[x][0] == min(mi)]
    mi = sorted(mi)
    x2 = [[a[x][0],mi[1]] for x in range(len(a)) if a[x][1] // a[x][0] == mi[1]]
    print(x)
    print(x2)
    x = x + x2
    x = sorted(x, key=lambda x: (x[1], -x[0]))
    x1 = [x[0] for x in x]
    print(x)
    return sum((x1)[:k]),max(x[0] * x[1] for x in x)


print(f("37test.txt"))
#(261, 910)

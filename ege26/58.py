def f(filename):
    file = open(filename)
    s,n = map(int,file.readline().split())
    a = [int(file.readline()) for _ in range(n)]
    a = [x for x in a if a.count(x) > 1]
    k = [a.count(x) for x in a]
    a = sorted(a)
    m = 0
    schet = 0
    v = []
    print(min(a),max(a))
    for i in range(len(a)):
        if a[i] * a.count(i) + m <= s:
            m += a[i] * a.count(i)
            v.append(a[i])
            schet += a.count(a[i])
    print(max(v))
    print(v)
    # a = sorted(a,reverse=True)
    # m = 0
    # schet2 = 0
    # for i in range(len(a)):
    #     if a[i] * a.count(i) + m <= s and schet2 == schet:

    return max(k),(max(v))




print(f("26data/26-58.txt"))

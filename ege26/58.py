def f(filename):
    file = open(filename)
    s,n = map(int,file.readline().split())
    a = [int(file.readline()) for _ in range(n)]
    a = [[x,a.count(x)] for x in sorted(set(a))]
    print(a)
    b = []
    v = 0
    print(min(a),max(a))
    for i in range(len(a)):
        if a[i][1] >= 2 and a[i][0] * a[i][1] + v <= s:
            v += a[i][0] * a[i][1]
            b.append(a[i])
            a[i] = [a[i][0], 0]
    a = [a[i] for i in range(len(a)) if a[i][1] != 0]
    print("выбранный товар", b)
    print("потрачено ",v) #потраченная сумма
    print("осталось", s-v)
    print("новый массив", a)
    b.append([44, 56])
    a[0] = [44, 124]
    b.append([64, 2])
    print("выбранный товар", b)
    v += 44*54 + 64*2
    print("потрачено ",v) #потраченная сумма
    print("осталось", s-v)
    print("новый массив", a)
    m = max(b,key=lambda x:x[1])
    k = max(b,key=lambda x:x[0])
    return k[0],m[1]




print(f("26data/26-58.txt"))

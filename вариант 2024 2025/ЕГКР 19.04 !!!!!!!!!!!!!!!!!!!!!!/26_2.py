def func(a):
    a = sorted(a)
    chet = [x for x in a if x % 2 == 0]
    nechet = [x for x in a if x % 2 == 1]
    t = 1
    m = 1
    for i in range(1, len(chet)):
        if chet[i] - 2 == chet[i-1]:
            t += 1
            m = max(m, t)
        else:
            t = 1
    t = 1
    for i in range(1, len(nechet)):
        if nechet[i] - 2 == nechet[i-1]:
            t += 1
            m = max(m, t)
        else:
            t = 1
    return m


def f(filename):
    file = open(filename)
    n = int(file.readline())
    d = dict()
    for _ in range(n):
        id, number = map(int, file.readline().split())
        d[id] = d.get(id, set()) | {number}
    b = [[k, func(d[k])] for k in d]
    b.sort(key=lambda x:(x[1], -x[0]) , reverse=True)
    return b[0]


print(*f("26test.txt"))
print(*f("26_21719.txt"))
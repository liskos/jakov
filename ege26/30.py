def f(filename):
    file = open(filename)
    n = int(file.readline())
    a = [int(file.readline()) for _ in range(n)]
    b = []
    b.append(a[0])
    for i in range(1,n-1):
        t = sorted(a[i-1:i+2])
        b.append(t[1])
    b.append(a[-1])
    print(a)
    v = 0
    print(b)
    for i in range(n):
        if a[i] > b[i]:
            v += a[i] - b[i]
    return b.count(min(b)),v


print(f("30test.txt"))
print(f("26data/26-J5.txt"))
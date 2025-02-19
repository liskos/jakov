def f(filename):
    file = open(filename)
    n = int(file.readline())
    a = [0] * 10000
    for _ in range(n):
        a[int(file.readline())] += 1
    s = sum([i*a[i] for i in range(1, 10000)])
    sr = s / n
    k = 0
    i = 0
    while k <= n // 2:
        i += 1
        k += a[i]
    med = i
    print(sr,med)
    print(sum(a[5004:5008]))
print(f("27test.txt"))
print(f("26data/26-J2.txt"))
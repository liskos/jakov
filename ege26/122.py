def f(filename):
    file = open(filename)
    k, n = map(int,file.readline().split())
    print("k", k, "|   n", n)
    a = [list(map(int,file.readline().split())) for _ in range(n)]
    a = sorted(a,key=lambda x:x[0])
    b = [[] for _ in range(50)]
    for i in range(n):
        t_begin, t_end = a[i]
        j = 0
        while len([r for r in b[j] if r >= t_begin]) == k:
            j += 1
        b[j] = [r for r in b[j] if r >= t_begin] + [t_end]
    ans1 = max(i for i in range(len(b)) if b[i]) + 1
    m = a[-1][0]
    s = 0
    for i in range(len(b)):
        s += len([r for r in b[i] if r > m])
    return ans1, s


print(f("122test.txt"))
# print(f("122test2.txt"))
print(f("26data/26-122.txt"))
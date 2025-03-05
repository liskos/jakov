def f(filename):
    file = open(filename)
    n = int(file.readline())
    k = int(file.readline())
    m = int(file.readline())
    a = [int(file.readline()) for _ in range(n)]
    a = sorted(a,reverse=True)
    xol = [0] * k
    for i in range(k):
        for x in a.copy():
            if x <= m - xol[i]:
                xol[i] += x
                a.remove(x)
            else:
                break
        for x in reversed(a.copy()):
            if x <= m - xol[i]:
                xol[i] += x
                a.remove(x)
            else:
                break
    ans1 = [i for i in range(k) if xol[i] != 0][-1]+ 1
    return ans1, m - xol[ans1-1]



print(f("138test.txt"))
print(f("26data/26-138.txt"))
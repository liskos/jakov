
def f(filename):
    file = open(filename)
    n, m = map(int, file.readline().split())
    a = [int(file.readline()) for _ in range(n)]
    kart = [x for x in a if x < 101]
    video = [x for x in a if x > 100]
    video = sorted(video)
    b = []
    for i in range(len(video)):
        if sum(b) >= m // 2:
            break
        else:
            b.append(video[i])
    print(sum((b)))
    c = []
    kart = sorted(kart)
    s = (m - sum(b))
    print(s)
    for i in range(len(kart)):
        if sum(c)+25 >= s:
            break
        else:
            c.append(kart[i])

    print(m - (sum(c) + sum(b)))
    return len(c)+len(b),max(c)
print(f("26data/26-61.txt"))
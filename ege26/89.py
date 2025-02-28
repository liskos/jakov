def f(filename):
    file = open(filename)
    n = int(file.readline())
    m = [int(file.readline()) for _ in range(n)]
    m = sorted(m)
    m.append(0)
    print(m)
    b = []
    k = 0
    d = []
    for i in range(len(m)-2):
        if abs(m[i] - m[i+1]) > 2:
            k += 1
            if k == 1:
                b.append(m[i])
        elif abs(m[i] - m[i+1]) <= 2:
            break
        else:
            d.append(k)
    print(b)
    return max(d),max(b)


print(f("89test.txt"))
print(f("26data/26-89.txt"))
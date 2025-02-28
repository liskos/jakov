def f(filename):
    file = open(filename)
    n,k = map(int,file.readline().split())
    m = [list(map(int,file.readline().split())) for _ in range(n)]
    m = sorted(m, key=lambda x: (-x[1],-x[2],x[0]))
    print(m[:50])
    b = []
    for x in range(len(m)-1):
        if m[x][2] == 6 and m[x+1][2] == 1 and m[x][0] == m[x+1][0]:
            b.append(m[x][1])

    return max(b),len(b)


print(f("81test.txt"))

print(f("26data/26-81.txt"))


def f(filename):
    file = open(filename)
    n = int(file.readline())
    r = [list(map(int,file.readline().split())) for _ in range(n)]
    r = sorted(r,key=lambda x:(x[0],x[1]))
    print(r)
    b = []
    k = 1
    ryad = 0
    for i in range(len(r)-1):
        if k > 1 and r[i][1] - r[i+1][1] == -1 and r[i][0] == r[i+1][0]:
            b.append([ryad,k+1])
        if r[i][1] - r[i+1][1] == -1 and r[i][0] == r[i+1][0]:
            k += 1
            ryad = r[i][0]

        else:
            b.append([ryad,k])
            k = 1
            ryad = 0
    b = sorted(b,key=lambda x:(-x[1],-x[0]))
    print(b)
    return b[0][0],b[0][1]
print(f("69test.txt"))

print(f("26data/26-69.txt"))
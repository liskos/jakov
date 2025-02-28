def f(filename):
    file = open(filename)
    n = int(file.readline())
    a = [list(map(int,file.readline().split())) for _ in range(n)]
    a = sorted(a,key=lambda x:(x[0],x[1]))
    print(a)
    k = 0
    b = []
    a.append([91231254,125125125])
    for i in range(len(a)-1):
        if a[i] == a[i+1]:
            0
        elif a[i][1] != a[i+1][1] and a[i][0] == a[i+1][0]:
            k += 1
        else:
            k += 1
            b.append([a[i][0],k])
            k = 0
    b = sorted(b,key=lambda x:(-x[1],-x[0]))
    print(b)
    return b[0][1],b[0][0]


print(f("73test.txt"))
print(f("26data/26-73.txt"))
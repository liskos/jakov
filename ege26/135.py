def f(filename):
    file = open(filename)
    n = int(file.readline())
    a = [list(map(int,file.readline().split())) for _ in range(n)]
    a = sorted(a,key=lambda x:(-x[0],-x[1]))
    print(a)
    b = []
    k = 0
    for i in range(n-2):
        if (a[i][1]-6 == a[i+1][1] and a[i+1][1] == a[i+2][1] + 6) and (a[i][0] == a[i+1][0] and a[i+1][0] == a[i+2][0]):
            b.append(a[i][0])
            k += 1

    return max(b),k




print(f("135.txt"))
print(f("26data/26-135.txt"))
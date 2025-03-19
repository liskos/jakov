def f(filename):
    file = open(filename)
    n = int(file.readline())
    a = [list(map(int,file.readline().split())) for _ in range(n)]
    a = sorted(a,key=lambda x:x[0])
    k = 1
    b = []
    for i in range(n-1):
        if a[i][0] == a[i+1][0] and a[i][1] % 2 == a[i+1][1] % 2 and a[i] != a[i+1]:
            k += a[i+1][1] - a[i][1]
        else:
            b.append([a[i-1][0],k//2+1])
            k = 1
    print(b)
    return max(b,key=lambda x:x[1])[1],max(b,key=lambda x:x[1])[0]

print(f("74test.txt"))
print(f("26data/26-73.txt"))
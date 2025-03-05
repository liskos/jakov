def f(filename):
    file = open(filename)
    n,k = map(int,file.readline().split())
    a = [list(map(int,file.readline().split())) for _ in range(n)]
    a = sorted(a,key=lambda x: (x[0],-x[1]))
    print(a)
    k = 0
    b = a[0]
    for i in range(n-1):
        print(b)
        if b[0] <= a[i+1][1] and b[1] >= a[i+1][1]:
            b = a[i]
            k += 1

        elif a[i+1][1] > b[1]:
            b = a[i]


    return k


print(f("139test.txt"))
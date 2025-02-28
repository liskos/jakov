def f(filename):
    file = open(filename)
    n,m = map(int,file.readline().split())
    a = [int(file.readline()) for _ in range(n)]
    a = sorted(a)
    d = 0
    k = 0
    b = []
    for i in range(len(a)-1):
        if a[i] - a[i+1] <= -3:
            k += 1
            d += a[i]
        elif a[i] - a[i-1] <= -3:
            k += 1
            d += a[i]
        else:
            b.append()
def f(filename):
    file = open(filename)
    n,s = map(int,file.readline().split())
    a = [int(file.readline()) for _ in range(n)]
    a = sorted(a,reverse=True)
    k = int(len(a)/6)
    b = sum(a[:k]) / 2
    a = sorted(a)
    for i in range(len(a)-1):
        if b + a[i] <= s:
            b +=
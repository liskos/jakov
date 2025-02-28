def f(filename):
    file = open(filename)
    n,d = map(int,file.readline().split())
    a = [int(file.readline()) for _ in range(n)]
    a = sorted(a,reverse=True)
    for i in range(len(a)-1):
        if a[i]
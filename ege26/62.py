def f(filename):
    file = open(filename)
    n,m = map(int,file.readline().split())
    a = [list(map(str,file.readline().split())) for _ in range(n)]
    print(a)
    for x in range(len(a)):
        a[x][0] = int(a[x][0])
    b = [x for x in range(len(a)) if a[x][1] == "Q"]


print(f("62test.txt"))
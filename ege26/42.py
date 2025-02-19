def f(filename):
    file = open(filename)
    n,s = map(int,file.readline().split())
    a = [list((file.readline().split())) for _ in range(n)]
    a = [[a[x][0],int(a[x][1]),int(a[x][2])] for x in range(len(a))]
    print(a)
    x = [x for x in range(len(a)) if a[x][0] == "Z"]


print(f("42test.txt"))
def f(filename):
    file = open(filename)
    n,s = map(int,file.readline().split())
    a = [list(map(int,file.readline().split())) for _ in range(n)]
    a = sorted(a, key=lambda x:x[0])
    b = []
    d = 0
    temp = [a[0][0],a[0][1]]
    for i in range(1,len(a)-1):
        if a[i][0] == a[i-1][0]:
            temp.append(a[i][1])
        else:
            b.append(temp)
            temp = [a[i][0],a[i][1]]
    b.append(temp)
    for x in range(len(b)):
        if sum(a[x][1:]) <= s:
            d.append()
        else:

    return b



print(f("71test.txt"))
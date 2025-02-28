def f(filename):
    file = open(filename)
    n,k = map(int,file.readline().split())
    s = ([list(map(int,file.readline().split())) for _ in range(n)])
    s = sorted(s,key=lambda x: (x[0],-x[1]))
    n = 0
    b = []
    s.append([0,99])
    print(s)
    for i in range(len(s)-1):

        if (s[i][1] - s[i+1][1])-1 == k and s[i][0] == s[i+1][0]:
            b.append([s[i][0],s[i+1][1]+1])
            n+=1
        if s[i][0] != s[i+1][0]:
            n = 0
    print(b)
    d = sorted(b,key=lambda x:-x[0])
    v = sorted(b,key=lambda x:(-x[0],x[1]))
    return d[0][0],v[0][1]


print(f("79test.txt"))
print(f("26data/26-79.txt"))
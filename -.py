def f(filename):
    file = open(filename)
    n = int(file.readline())
    s = [list(map(int,file.readline().split())) for _ in range(n)]
    s = sorted(s, key=lambda x:(-x[0],-x[1]))
    print(s)
    b = []
    for i in range(len(s)-1):
        if s[i][1] - s[i+1][1] == 14 and s[i][0] == s[i+1][0]:
            b.append([s[i][0],s[i+1][1]+1])
    print(b)
    b = sorted(b,key=lambda x:(-x[0],x[1]))
    return b[0][0],b[0][1]

print(f("учёба/26_7274.txt"))
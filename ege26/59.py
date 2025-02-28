def f(filename):
    file = open(filename)
    n = int(file.readline())
    r = [list(map(int,file.readline().split())) for _ in range(n)]
    r = sorted(r,key=lambda x:x[1])
    r = sorted(r,key=lambda x:-x[0])
    print(r)
    b = []
    for i in range(len(r)-1):
        if abs(r[i][1] - r[i+1][1]) == 3 and r[i][0] == r[i+1][0]:
            b.append([r[i][0],r[i+1][1]-2])
    n = sorted(b,key=lambda x: -x[0])
    print(b)
    m = sorted(b,key=lambda x: x[1])
    return n[0][0],m[0][1]


print(f("59test.txt"))

print(f("26data/26-59.txt"))
def f(filename):
    file = open(filename)
    n = int(file.readline())
    a = [list(map(int,file.readline().split())) for _ in range(n)]
    a = sorted(a,key=lambda x:(x[0],x[1]))
    b = []
    k = 1
    v = 0
    for i in range(len(a)-1):
        if a[i][0] == a[i+1][0] and a[i+1][1] - a[i][1] == 2:
            k += 1
            v = a[i][0]
        elif a[i] == a[i+1]:
            pass
        else:
            b.append([v,k])
            v = 0
            k = 1

    b.append([v,k])
    b = sorted(b,key=lambda x:-x[1])[0]
    return b

print(f("26test.txt"))
print(f("26_21719.txt"))
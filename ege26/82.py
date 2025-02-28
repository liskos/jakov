def f(filename):
    file = open(filename)
    n = int(file.readline())
    a = [list(map(int,file.readline().split())) for _ in range(n)]
    a = sorted(a,key=lambda x:(x[0],x[1]))
    a.append([1234,5121])
    k = 0
    b = []
    for i in range(len(a)-1):
        if a[i][0] == a[i-1][0] and a[i][1] == a[i-1][1]:
            0
        elif a[i][1] % 2 == 0 and a[i][0] == a[i+1][0]:
            k += 1
        elif a[i][1] % 2 == 0 and a[i][0] != a[i+1][0]:
            k += 1
            b.append([k,a[i][0]])
            k = 0
        else:
            0
    print(b)
    b = sorted(b,key=lambda x:(-x[0],x[1]))

    return b[0][0],b[0][1]


# print(f("82test.txt"))
# print(f("82test2.txt"))
print(f("26data/26-82.txt"))
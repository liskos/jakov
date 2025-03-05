def f(filename):
    file = open(filename)
    n = int(file.readline())
    a = [list(map(int,file.readline().split())) for _ in range(n)]
    a = sorted(a,key=lambda x:(x[0],x[1]))
    perv = min(a,key=lambda x:x[1])
    print(a)
    print(perv)
    a.remove(perv)
    k = 1
    b = []
    for i in range(len(a)):
        if perv[1] <= a[i][0]:
            b.append(perv[1])
            perv = a[i]
            k += 1


    return k,b[0]




print(f("141test.txt"))
print(f("26data/26-141.txt"))
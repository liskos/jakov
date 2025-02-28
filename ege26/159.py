def f(filename):
    file = open(filename)
    n = int(file.readline())
    a = [list(map(int, file.readline().split())) for _ in range(n)]  # Считываем n строк и преобразуем в список списков
    a = sorted(a,key=lambda x:(x[0],x[1]))
    print(a[1:50])
    a.append([0,20])
    b = []
    k = 0
    c = 0
    for i in range(len(a)-1):

        if a[i][1] - a[i+1][1] == -1 and a[i][0] == a[i+1][0]:
            c = a[i][0]
            k += 1
        else:
            b.append([c,k])
            c = 0
            k = 0
    b = sorted(b,key=lambda x:(-x[1],x[0]))
    return b[0]

print(f("26data/26-159.txt"))
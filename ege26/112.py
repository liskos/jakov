def f(filename):
    file = open(filename)
    b,n = map(int,file.readline().split())
    k = 0
    a = []
    b = [[1440]]
    for i in range(n):
        k += 1
        nachalo,kones = map(int,file.readline().split())
        a.append([nachalo,kones,k])
    a = sorted(a,key=lambda x:(x[0],x[1],x[2]))
    print(a)
    for i in range(n):






print(f("112test.txt"))
print(f("26data/26-112.txt"))
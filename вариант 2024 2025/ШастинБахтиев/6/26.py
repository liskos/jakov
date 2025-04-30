def f(filename):
    file = open(filename)
    n = int(file.readline())
    a = [list(map(int,file.readline().split())) for _ in range(n)]
    a = sorted(a,key=lambda x:(x[1],x[2]))
    print(a)
    k = 0
    priexal = [0]
    b = []
    for i in range(len(a)-1):
        if a[i][2] > a[i+1][1]:
            k += 1
            priexal.append(a[i][-1])
        b.append(k)
        if a[i][1] > min(priexal):
            k -= 1
            priexal.remove(min(priexal))
    d = max(b)
    b = [x for x in b if x == d]
    return len(b)


print(f("26_18492.txt"))
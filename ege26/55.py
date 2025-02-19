def f(filename):
    file = open(filename)
    n,s = map(int,file.readline().split())
    a = [int(file.readline()) for _ in range(n)]
    a = sorted(a,reverse=True)
    k = 0
    b = []
    for x in range(len(a)):
        if a[x] + a[x+1] <= s:
            a.pop(x)
            a.pop(x+1)
            k += 1
    for x in range(len(a)):
        if a[x] + a[x+1] <= s:
            a.pop(x)
            a.pop(x+1)
            k += 1
            b.append([a[x],1])
        else:
            a.pop(x)
            k+=1
            b.append([a[x],0])

    b = sorted(b,key=lambda x: x[1])
    return k,b[0]


print(f("55test.txt"))
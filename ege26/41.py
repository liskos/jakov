def f(filename):
    file = open(filename)
    d,e,n = map(int,file.readline().split())
    a = [int(file.readline()) for _ in range(n)]
    d = [x for x in a if x > 500]
    a = [x for x in a if d.count(x) == 0]
    a = sorted(a)
    k = 0
    for x in a:
        if x + s <= e:
            k+=1
            s.append(x)
        else:
            ()

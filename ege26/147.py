    def f(filename):
        file = open(filename)
        n = int(file.readline())
        a = [list(map(int,file.readline().split())) for _ in range(n)]
        a = sorted(a,key=lambda x:(x[0],x[1]))
        print(a)
        b = [a[0][0]+a[0][1]]
        k = 1
        ans2 = []
        for x in a[1:]:
            if min(b) <= x[0]:
                b.append(x[1]+x[0])
                b.remove(min(b))
            else:
                k += 1
                b.append(x[0]+x[1])
            print(k,b)
        return k


    print(f("147test.txt"))
    print(f("26data/26-147.txt"))
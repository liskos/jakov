def f(filename):
    file = open(filename)
    s,n = map(int,file.readline().split())
    a = [int(file.readline()) for _ in range(n)]
    a = sorted(a)
    print(a)
    ob = []
    for x in range(len(a)):
        if sum(ob) + a[-1] + a[0] <= s:
            ob.append(a[-1])
            ob.append(a[0])
            a.pop(-1)
            a.pop(0)
        elif sum(ob) + a[0] <= s:
            x = max([x for x in a if s - sum(ob) >= x])
            ob.append(x)
            a.pop(0)
    print(len(ob),ob[-1])



print(f("38test.txt"))
print(f("26data/26-j9.txt"))
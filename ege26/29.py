def f(filename):
    file = open(filename)
    n = int(file.readline())
    a = [int(file.readline()) for _ in range(n)]
    a = sorted(a,reverse=True)
    print(a)
    k = int(len(a) * 0.1)
    ob = a[k:-k]
    print(ob)
    return sum(ob),max(ob)


print(f("29test.txt"))
print(f('26data/26-j4.txt'))
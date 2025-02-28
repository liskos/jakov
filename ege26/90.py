def f(filename):
    file = open(filename)
    n = int(file.readline())
    a = [int(file.readline()) for _ in range(n)]
    a = sorted(a)
    k = int(len(a) / 4)
    b = sum(a[:k])*0.5 + sum(a[k:])
    a = sorted(a,reverse=True)
    c = sum(a[:k])*0.5 + sum(a[k:])


    return c,b

print(f("90test.txt"))
print(f("26data/26-90.txt"))
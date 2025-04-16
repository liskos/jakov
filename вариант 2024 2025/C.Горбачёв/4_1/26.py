def f(filename):
    file = open(filename)
    n = int(file.readline())
    a = [int(file.readline()) for _ in range(n)]
    a = sorted(a,reverse=True)
    print(a)
    skid = sum(a[:n//5]) * 0.5 + sum(a[n//5:])
    neygadal = sum(a) - sum(a[4::5])*0.5
    return skid,neygadal




print((f("26test.txt")))
print(f("26_18339.txt"))
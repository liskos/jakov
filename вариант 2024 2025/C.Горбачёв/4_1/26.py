def f(filename):
    file = open(filename)
    n = int(file.readline())
    a = [int(file.readline()) for _ in range(n)]
    a = sorted(a,reverse=True)
    print(a)
    skid = sum(a[:n//5]) * 0.5 + sum(a[n//5:])
    neygadal = [a[x] for x in range(len(a)) if x % 4 == 0 and x != 0]
    neygadal = sum(neygadal[:n//5]) * 0.5 + sum(a[:n]) - sum(neygadal)
    return skid,neygadal




print((f("26test.txt")))
print(f("26_18339.txt"))
def f(filename):
    file = open(filename)
    n = int(file.readline())
    a = [int(file.readline()) for _ in range(n)]
    a = sorted(a,reverse=True)
    b = [a[x] for x in range (len(a)-1) if a[x+1] <= a[x]]

    return len(b),




print(f("dosrok23test.txt"))
print(f("26data/26_15341.txt"))
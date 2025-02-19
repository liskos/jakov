def f(filename):
    file = open(filename)
    n = int(file.readline())
    a = [int(file.readline()) for _ in range(n)]
    a = sorted(a,reverse=True)
    k = int(len(a) * 0.2)
    bogat = a[:k]
    a = a[k:]
    pr = sum(a) * 0.6
    pr = pr // len(a)
    pr = sum(a) * 0.6 // pr
    print(sum(bogat)*0.8,min(a)*pr//20)



print(f("35test.txt"))
print(f("26data/26-j7.txt"))


#143518 401
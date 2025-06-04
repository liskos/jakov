def f(filename):
    file = open(filename)
    n = int(file.readline())
    a = [int(file.readline()) for _ in range(n)]
    print(len(a))
    b = []
    s = 0
    k = 0
    for i in range(len(a)):
        b.append(a[i])
        b.sort()
        d = b.index(a[i]) #index
        if len(b) == 1:
            continue
        if d == 0:
            k += 1
            s += b[1]
        elif d == len(b)-1:
            s += b[-2]
            k += 1
        else:
            s += b[d+1] + b[d-1]
            k += 2
    return k,s

print(f('26test.txt'))
print(f("26.txt"))
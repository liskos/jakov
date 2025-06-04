def f(filename):
    file = open(filename)
    n = int(file.readline())
    a = [int(file.readline()) for _ in range(n)]
    print(len(a))
    b = []
    s = 0
    k = 1
    d = 0
    for i in range(len(a)):
        b.append(a[i])
        b.sort()
        d = max([item for item in range(len(b)) if a[i] == b[item]]) #index
        if i == 0:
            continue
        if a[i] == b[-1]:
            s += b[-2]
            k += 1
        else:
            s += b[d+1] + b[d-1]
            k += 1
    return k,s,b

print(f('26test.txt'))
print(f("26.txt"))
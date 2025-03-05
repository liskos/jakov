def f(filename):
    file = open(filename)
    n =int(file.readline())
    a = [list(map(int,file.readline().split())) for _ in range(n)]
    a = sorted(a, key=lambda x: x[1],)
    k = 0
    a.append([1,1])
    print(a)
    last = 0
    for start,end in a:
        if start >= last:
            k += 1
            last = end

    return k,last


print(f("128test.txt"))
print(f("26data/26-128.txt"))
def f(filename):
    file = open(filename)
    n = int(file.readline())
    sl = [int(file.readline()) for _ in range(n)]
    sl = sorted(sl)
    print(sl)

    k = 0
    b = []
    for i in range(len(sl)):
        if sl[i] <= k+1:
            k+=sl[i]
        else:
            b.append(sl[i]-k-1)
            k+=sl[i]
    print(b)
    return len(b),sum(b)





print(f("70test.txt"))
print(f("70test2.txt"))
print(f("26data/26-70.txt"))
def f(filename):
    file = open(filename)
    s,n = map(int,file.readline().split())
    a = sorted([int(file.readline()) for _ in range(n)],reverse=True)
    b = []
    print(a)
    for i in range(n):
        if a[i] + sum(b) <= s:
            b.append(a[i])

    return len(b),min(b)



print(f("28test.txt"))

print(f("26data/26-J3.txt"))
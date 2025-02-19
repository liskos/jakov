def f(filename):
    file = open(filename)
    n = int(file.readline())
    a = [int(file.readline()) for _ in range(n)]
    ob = sum(a) * 0.9
    a = sorted(a,reverse=True)
    new = a.copy()
    for i in range(n):
        new[i] = a[i] * 0.8
        if sum(new) <= ob:
            break
    k = n - (i+1)
    new[i] = a[i]
    new[i+1]= a[i+1] * 0.8
    if sum(new) > ob:
        return k, a[i+1]
    while sum(new) <= ob and i > 0:
        i = i - 1
        new[i+1] = a[i+1] * 0.8
        new[i] = a[i]
    return k,a[i+1]

print(f("34test.txt"))
print(f("26data/26-j6.txt"))
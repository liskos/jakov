def f(filename):
    file = open(filename)
    v,k,n = map(int,file.readline().split())
    p = [int(file.readline()) for _ in range(n)]
    b = []
    p = sorted(p,reverse=True)
    otv = []
    while k != 0:
        b.append(v)
        k -= 1
    print(b)
    for i in range(len(p)):
        max_ind = b.index(max(b))
        if p[i] <= max(b):
            b[max_ind] -= p[i]
        else:
            otv.append(p[i])
    print(otv)
    return sum(otv),len(otv)
print(f("56test.txt"))

print(f("26data/26-56.txt"))
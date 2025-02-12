def f(filename):
    file = open(filename)
    s,n = map(int,file.readline().split())
    a = [int(file.readline()) for _ in range(n)]
    a = sorted(a)
    v = []
    for x in a:
        if sum(v) + x <= s:
            v.append(x)
        else:
            break
    sv = s - sum(v)+v[-1]
    b = max(x for x in a if x <= sv)
    return len(v),b

print(*f("26data/26-1.txt"))
print("---------------------")
print(*f("1test.txt"))
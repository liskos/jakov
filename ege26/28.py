def f(filename):
    file = open(filename)
    s,n = map(int,file.readline().split())
    a = [int(file.readline()) for _ in range(n)]
    b = []
    for x in a:
        if sum(b) + max(a) <= s:
            b.append(max(a))
            a.remove(max(a))
        if sum(b) + min(a) <= s and sum(b) + max(a) > s:
            b.append(min(a))
            a.remove(min(a))
    return len(b),min(b)



print(f("28test.txt"))

print(f("26data/26-J3.txt"))
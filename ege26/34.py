def f(filename):
    file = open(filename)
    n = int(file.readline())
    a = [int(file.readline()) for _ in range(n)]
    ob = sum(a) * 0.9
    a = sorted(a,reverse=True)
    c = a
    for x in a:
        if sum(c) <= ob:
            break
        else:
            v = a[0]
            c.append(v*0.8)
            c.remove(x)
            a.remove(x)
    return len(a),max(a)

print(f("34test.txt"))
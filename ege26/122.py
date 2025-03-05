def f(filename):
    file = open(filename)
    d,n = map(int,file.readline().split())
    a = [list(map(int,file.readline().split())) for _ in range(n)]
    k = 0
    b = []
    for i in range(n):
        print(b)
        if len(b) > 0 and min(b) < a[i][0]:
            k -= 1
            b.remove(min(b))
        k += 1
        b.append(a[i][1])


    return int(k / d + 0.9999),k


print(f("122test.txt"))
# print(f("122test2.txt"))
print(f("26data/26-122.txt"))
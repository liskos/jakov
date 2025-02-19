def f(filename):
    file = open(filename)
    n = int(file.readline())
    a = [int(file.readline()) for _ in range(n)]
    b = [x for x in a if x > 150]
    b = sorted(b)
    k = int(len(b)//2)
    skid = int(sum(b[:k])*0.2)
    return sum(a) - skid,b[:k][-1]


print(f("32test.txt"))
print("!!!!!!!!!!")
print(f("26data/26-s1.txt"))
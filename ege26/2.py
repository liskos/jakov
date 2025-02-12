def f(filename):
    file = open(filename)
    n,k = map(int,file.readline().split())
    a = [int(file.readline()) for _ in range(n)]
    a = sorted(a,reverse=True)
    skidka = a[:k]
    bezsk = a[k:]

    print(n,k)
    print(a)

    return max(bezsk),sum(skidka)*0.2


print(f("26data/26-k1.txt"))
print(f("2test.txt"))



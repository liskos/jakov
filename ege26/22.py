def f(filename):
    file = open(filename)
    n,k = map(int,file.readline().split())
    a = [int(file.readline()) for _ in range(n)]
    a = sorted(a,reverse=True)
    nedost1 = a[:k]
    nedost2 = a[-1:k]
    dost = a[k:-k]
    print(dost)
    return max(dost),sum(dost) / len(dost)


print(f("22test.txt"))
print("арбузыыыыыыыыыыыыыыыыы")
print(f("26data/26-k2.txt"))

#957 501
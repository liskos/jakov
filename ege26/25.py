def f(filename):
    file = open(filename)
    n,k,m = map(int,file.readline().split())
    a = [int(file.readline())for _ in range(n)]
    a = sorted(a,reverse=True)
    print(a)
    dorogo = a[:m]
    a = sorted(a)
    budzet = a[:k]
    print(budzet)

    return min(dorogo),sum(budzet)/len(budzet)


print(f('25test.txt'))
print("AAA")
print(f("26data/26-k5.txt"))
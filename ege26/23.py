def f(filename):
    file = open(filename)
    n,k,m = map(int,file.readline().split())
    a = [int(file.readline()) for _ in range(n)]
    a = sorted(a,reverse=True)
    pobeda = a[:k]
    prizer = a[k:m+k]
    return min(prizer),min(pobeda)



print(f("23test.txt"))
print("арбузыыыыыыыыыыыыыыыыы")
print(f("26data/26-k3.txt"))
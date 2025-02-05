def prost(n):
    a = [True] * n
    a[0] = False
    a[1] = False
    for i in range(2,n):
        if a[i]:
            for g in range(i**2,n,i):
                a[g] = False
    r = [i for i in range(n) if a[i]]
    return r


b = prost(20000)

for n in range(2,20000+1):
    k = 0
    for i in b:
        if n % i == 0:
            k+=1
        if i > n:
            break
    if k == 5:
        print(n)
        break

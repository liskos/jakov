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

p = prost(1000000)

# def f(n):
#     global p
#     if n == 1:
#         return set()
#     for i in p:
#         if n % i == 0:
#             return {i} | f(n//i)

a = []
for i in range(2,1000000+1):
    n = i
    sss = set()
    for x in p:
        if n % x == 0:
            sss.add(x)
            while n % x == 0:
                n = n // x
        if n == 1:
            break
    sss = sum(sss)
    if sss % 24453 == 0:
        a.append([i,sss])
    if i % 10000 == 0:
        print(i // 10000, "%")
for i in a:
    print(*i)

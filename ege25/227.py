def prost(n):
    a = [True] * 3000
    a[0] = False
    a[1] = False
    for i in range(2,3000):
        if a[i]:
            for g in range(i**2,3000,i):
                a[g] = False
    r = [i for i in range(3000) if a[i]]
    return r
b = prost(1)
def delitel(n):
    a = set()
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    x = [x for x in a if b.count(x)]
    return x


for i in range(200,2023):
    if min(delitel(i)) > 10 and len(delitel(i)) > 1:
        print(i,min(delitel(i)))

# 1961 37
# 1963 13
# 1969 11
# 1991 11
# 2021 43

def prost(n):
    a = [True] * 20222023
    a[0] = False
    a[1] = False
    for i in range(2,20222022+1):
        if a[i]:
            for g in range(i**2,20222022+1,i):
                a[g] = False
    r = [i for i in range(20222022+1) if a[i]]
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


for i in range(2022,20222022+1):
    if min(delitel(i)) > 100 and len(delitel(i)) > 1:
        print(i,min(delitel(i)))

#2021 43
#2017 2017
#2011 2011
#2003 2003
#1999 1999

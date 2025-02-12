def prost(n):
    a = [True] * 100000
    a[0] = False
    a[1] = False
    for i in range(2,100000):
        if a[i]:
            for g in range(i**2,100000,i):
                a[g] = False
    r = [i for i in range(100000) if a[i]]
    return r
b = prost(1)
b = [x for x in b if sum(map(int,str(x))) > 35]
print(b)
for n in range(33333,55555+1):
    if b.count(n):
        print(n,sum(map(int,str(n))))

#39799 37
# 39979 37
# 39989 38
# 48799 37
# 48889 37
# 48989 38
# 49789 37
# 49999 40
def prost(n):
    a = [True] * 5000000
    a[0] = False
    a[1] = False
    for i in range(2,5000000):
        if a[i]:
            for g in range(i**2,5000000,i):
                a[g] = False
    r = [i for i in range(5000000) if a[i]]
    return r


b = prost(1)
p = 0
for n in range(1371085,1371135):
    if b.count(n):
        p+=1
        print(p,n)

# 1 1371089
# 2 1371103
# 3 1371107
# 4 1371113
# 5 1371119
# 6 1371121
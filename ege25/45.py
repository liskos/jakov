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
for n in range(4301614,4301718):
    if b.count(n):
        p+= 1
        print(p,n)

# 1 4301623
# # 2 4301669
# # 3 4301699
# # 4 4301701
# # 5 4301707
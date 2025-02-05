def prost(n):
    a = [True] * 5000000
    a[0] = False
    a[1] = True
    for i in range(2,5000000):
        if a[i]:
            for g in range(i**2,5000000,i):
                a[g] = False
    r = [i for i in range(5000000) if a[i]]
    return r

b = prost(1)
p = 0

for n in range(3614033,3614116+1):
    if b.count(n):
        p+=1
        print(p,n)

# 1 3614033
# 2 3614041
# 3 3614057
# 4 3614087
# 5 3614099
# 6 3614101
# 7 3614111
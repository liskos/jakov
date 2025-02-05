def prost(n):
    a = [True] * 7000000
    a[0] = False
    a[1] = True
    for i in range(2,7000000):
        if a[i]:
            for g in range(i**2,7000000,i):
                a[g] = False
    r = [i for i in range(7000000) if a[i]]
    return r

b = prost(1)
p = 0

for n in range(5336748,5336834+1):
    if b.count(n):
        p+=1
        print(p,n)

# 1 5336753
# 2 5336761
# 3 5336789
# 4 5336797
# 5 5336801
# 6 5336813
# 7 5336831
# 8 5336833

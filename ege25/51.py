def prost(n):
    a = [True] * 5000000
    a[0] = False
    a[1] = False
    for i in range(2,5000000):
        if a[i]:
            for g in range(i**2,5000000,i):
                a[g] = False
    r = [i for i in range(5000000)if a[i]]
    return r


b = prost(1)
p = 0
for n in range(3144472,3144601):
    if b.count(n):
        p+=1
        print(p,n)


#1 3144509
# 2 3144527
# 3 3144529
# 4 3144539
# 5 3144551
# 6 3144571
# 7 3144587
# 8 3144599
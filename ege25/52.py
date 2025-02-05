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

for n in range(4409962,4410102):
    if b.count(n):
        p+=1
        print(p,n)

# 1 4409981
# 2 4410019
# 3 4410041
# 4 4410047
# 5 4410061
# 6 4410079
# 7 4410097
# 8 4410101
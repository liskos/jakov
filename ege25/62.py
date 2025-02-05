def prost(chisla):
    a = [True] * 3000000
    a[0] = False
    a[1] = False
    for i in range(2,3000000):
        if a[i]:
            for g in range(i**2,3000000,i):
                a[g] = False
    r = [i for i in range(3000000) if a[i]]
    return r


b = prost(1)
p = 0
d = []

for n in range(1532040,1532160+1):
    if b.count(n):
        d.append(n)

d = sorted(d,reverse=True)
for h in d:
    p+=1
    print(p,h)

# 1 1532143
# 2 1532131
# 3 1532123
# 4 1532117
# 5 1532107
# 6 1532093
# 7 1532081
# 8 1532077
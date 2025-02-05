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

for n in range(2532000,2532160+1):
    if b.count(n):
        d.append(n)

d = sorted(d,reverse=True)
for h in d:
    p+=1
    print(p,h)

# 1 2532157
# 2 2532143
# 3 2532137
# 4 2532113
# 5 2532109
# 6 2532107
# 7 2532083
# 8 2532071
# 9 2532067
# 10 2532007

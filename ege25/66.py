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

for n in range(194441,196500+1):
    if b.count(n):
        d.append(n)
for h in d:
    if h % 100 == 93:
        p += 1
        print(p,h)

# 1 195193
# 2 195493
# 3 195593
# 4 195893
# 5 196193
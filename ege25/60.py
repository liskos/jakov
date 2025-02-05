def prost_chisla(n):
    a = [True] * 8000000
    a[0] = False
    a[1] = False
    for i in range(2,8000000):
        if a[i]:
            for g in range(i**2,8000000,i):
                a[g] = False
    r = [i for i in range(8000000) if a[i]]
    return r


b = prost_chisla(1)
p = []
for n in range(3532000,3532160+1):
    if b.count(n):
        p.append(n)
k = 0
p = sorted(p,reverse=True)
for i in p:
    k+=1
    print(k,i)

# 1 3532147
# 2 3532121
# 3 3532103
# 4 3532091
# 5 3532049
# 6 3532033
# 7 3532021
# 8 3532019
# 9 3532007
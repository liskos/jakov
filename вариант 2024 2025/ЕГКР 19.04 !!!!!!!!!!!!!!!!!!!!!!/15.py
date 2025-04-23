k = 10
b = range(36*k,75*k+1)
c = range(60*k,110*k+1)

a1_best = 0
a2_best = 50000

for a1 in range(30*k+1,40*k):
    for a2 in range(95*k,102*k+1):
        a = range(a1,a2+1)
        if all([(x in a) or ((x in b) == (x in c)) for x in range(1,100*k)]):
            if a2 - a1 < a2_best - a1_best:
                a2_best = a2
                a1_best = a1


print(a1_best/k,a2_best/k,(a2_best-a1_best)/k)


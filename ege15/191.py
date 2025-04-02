k = 10
p = range(10*k,18*k+1)
q = range(8*k,30*k+1)

a1_best = 0
a2_best = 500
for a1 in range(6*k,13*k+1):
    for a2 in range(14*k,24*k+1):
        a = range(a1,a2+1)
        if all([(x in a) or (not(x in p) or (x not in q)) for x in range(1,100*k)]):
            if a2 - a1 < a2_best - a1_best:
                a1_best = a1
                a2_best = a2


print(a1_best/k,a2_best/k,(a2_best-a1_best)/k)

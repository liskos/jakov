k = 10
p = range(15*k,142*k+1)
q = range(38*k,167*k+1)
a1_best = 0
a2_best = 5000*k
for a1 in range(35*k,40*k+1):
    for a2 in range(140*k,145*k+1):
        a = range(a1,a2+1)
        if all([(not(x in q) or(not(not(x in a) and(x in p)) or (not(x in q)))) for x in range(1*k,300*k)]):
            if a2_best - a1_best > a2 - a1:
                a2_best = a2
                a1_best = a1

print(a1_best/k,a2_best/k,(a2_best-a1_best)/k)



k = 10
p = range(12*k,24*k+1)
q = range(18*k,30*k+1)

a1_best = 0
a2_best = 500
for a1 in range(15*k,20*k+1):
    for a2 in range(20*k,25*k+1):
        a = range(a1,a2+1)
        if all([not(x not in a) or (not(x in p) or (x not in q)) for x in range(1,100*k)]):
            if a2 - a1 < a2_best - a1_best:
                a2_best = a2
                a1_best = a1


print(a1_best/k,a2_best/k,(a2_best-a1_best)/k)


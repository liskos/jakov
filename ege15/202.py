k = 1
p = range(7*k,15*k+1)
q = range(12*k,25*k+1)

a1_best = 0
a2_best = 500
for a1 in range(1*k,100*k+1):
    for a2 in range(a1*k,100*k+1):
        a = range(a1,a2+1)
        if all([((x not in p) or (x in a)) and ((x not in q) or (x in a)) for x in range(1,100*k)]):
            if a1 - a2 < a2_best - a1_best:
                a1_best = a1
                a2_best = a2


print(a1_best/k,a2_best/k,(a2_best-a1_best)/k)
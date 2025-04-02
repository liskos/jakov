k = 10
p = range(15*k,30*k+1)
q = range(8*k,25*k+1)

a1_best = 0
a2_best = 500
for a1 in range(1*k,100*k+1):
    for a2 in range(a1*k,100*k+1):
        a = range(a1,a2+1)
        if all([not((x in p) and (x in q)) or (x in a) for x in range(1,100*k)]):
            if a2 - a1 < a2_best - a1_best:
                a1_best = a1
                a2_best = a2


print(a1_best/k,a2_best/k,(a2_best-a1_best)/k)

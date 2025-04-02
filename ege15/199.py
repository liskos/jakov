k = 1
p = range(22*k,35*k+1)
q = range(15*k,30*k+1)

a1_best = 0
a2_best = 500
for a1 in range(12*k,18*k+1):
    for a2 in range(31*k,37*k+1):
        a = range(a1,a2+1)
        if all([(not(x in p) or (x in a)) and ((x not in q) or (x in a))for x in range(1,100*k)]):
            if a2 - a1 < a2_best - a1_best:
                a1_best = a1
                a2_best = a2


print(a1_best/k,a2_best/k,(a2_best-a1_best)/k)
#19.0 25.0 6.0

k = 10
p = range(21*k,35*k+1)
q = range(8*k,25*k+1)

a1_best = 0
a2_best = 0
for a1 in range(22*k,28*k+1):
    for a2 in range(32*k,38*k+1):
        a = range(a1,a2+1)
        if all([not((x not in p) or (x  in q)) or (x not in a) for x in range(1,100*k)]):
            if a2 - a1 > a2_best - a1_best:
                a1_best = a1
                a2_best = a2


print(a1_best/k,a2_best/k,(a2_best-a1_best)/k)
#19.0 25.0 6.0

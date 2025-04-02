k = 10
p = range(12*k,28*k+1)
q = range(8*k,16*k+1)

a1_best = 0
a2_best = 0
for a1 in range(13*k,19*k+1):
    for a2 in range(25*k,31*k+1):
        a = range(a1,a2+1)
        if all([not(x in a) or((x in p) and (x not in q)) for x in range(1,100*k)]):
            if a2 - a1 > a2_best - a1_best:
                a1_best = a1
                a2_best = a2


print(a1_best/k,a2_best/k,(a2_best-a1_best)/k)

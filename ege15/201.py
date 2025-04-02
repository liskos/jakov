k = 10
p = range(0*k,10*k+1)
q = range(25*k,50*k+1)

a1_best = 0
a2_best = 500
for a1 in range(-2*k,6*k+1):
    for a2 in range(97*k,103*k+1):
        a = range(a1,a2+1)
        if all([not(x not in a) or ((x not in p) and (x not in q)) for x in range(1,100*k)]):
            if a1 - a2 < a2_best - a1_best:
                a1_best = a1
                a2_best = a2


print(a1_best/k,a2_best/k,(a2_best-a1_best)/k)
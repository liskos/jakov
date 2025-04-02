k = 10
p = range(8*k,16*k+1)
q = range(25*k,40*k+1)

a1_best = 0
a2_best = 500
for a1 in range(4*k,12*k+1):
    for a2 in range(88*k,94*k+1):
        a = range(a1,a2+1)
        if all([not((x in p) or (x in q)) or (x in a) for x in range(1,100*k)]):
            if a1 - a2 < a2_best - a1_best:
                a1_best = a1
                a2_best = a2


print(a1_best/k,a2_best/k,(a2_best-a1_best)/k)
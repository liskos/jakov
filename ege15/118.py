k = 10
p = range(3*k,15*k+1)
q = range(14*k,25*k+1)

a1_best = 0
a2_best = 0
for a1 in range(1*k,7*k+1):
    for a2 in range(7*k,15*k+1):
        a = range(a1,a2+1)
        if all([not((x in p) == (x in q)) or not(x in a) for x in range(1,100*k)]):
            if a2 - a1 > a2_best - a1_best:
                a1_best = a1
                a2_best = a2


print(a1_best/k,a2_best/k,(a2_best-a1_best)/k)

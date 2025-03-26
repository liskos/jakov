k = 10
p = range(12*k,24*k+1)
q = range(18*k,30*k+1)

a1_best = 0
a2_best = 0
for a1 in range(8*k,27*k+1):
    for a2 in range(30*k,34*k+1):
        a = range(a1,a2+1)
        if all([not(x not in a) or (not(x in p) or (x not in q)) for x in range(1,1000)]):
            if a2 - a1 > a2_best - a1_best:
                a2_best = a2
                a1_best = a1


print(a1_best/k,a2_best/k,(a2_best-a1_best)/k)


k = 10
p = range(25*k,50*k+1)
q = range(32*k,47*k+1)

a1_best = 0
a2_best = 0
for a1 in range(30*k,35*k+1):
    for a2 in range(45*k,49*k+1):
        a = range(a1,a2+1)
        if all([not((x in a) or not(x in p)) or(not(x in a) or (x in q)) for x in range(1,100*k)]):
            if a2 - a1 > a2_best - a1_best:
                a2_best = a2
                a1_best = a1
print(a1_best/k,a2_best/k,(a2_best - a1_best)/k)
k = 30
p = range(15*k,33*k+1)
q = range(45*k,68*k+1)

a1_best = 0
a2_best = 0
for a1 in range(42*k,48*k+1):
    for a2 in range(64*k,71*k+1):
        a = range(a1,a2+1)
        if all([not((x in a) and not(x in q)) or ((x in p) or (x in q)) for x in range(1,100*k)]):
            if a2 - a1 > a2_best - a1_best:
                a1_best = a1
                a2_best = a2


print(a1_best/k,a2_best/k,(a2_best-a1_best)/k)

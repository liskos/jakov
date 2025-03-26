k = 10
p = range(12*k,26*k+1)
q = range(30*k,53*k+1)

a1_best = 0
a2_best = 0
for a1 in range(9*k,29*k):
    for a2 in range(26*k,56*k):
        a = range(a1,a2+1)
        if all([(not(x in a) or (x in p)) or (x in q) for x in range(1,100*k)]):
            if a2 - a1 > a2_best - a1_best:
                a2_best = a2
                a1_best = a1
print(a1_best/k,a2_best/k,(a2_best-a1_best)/k)
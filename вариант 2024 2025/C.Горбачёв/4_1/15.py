k = 10
p = range(17*k,61*k+1)
q = range(39*k,91*k+1)
a1_best = 0
a2_best = 500

for a1 in range(58*k,65*k+1):
    for a2 in range(87*k,94*k+1):
        a = range(a1,a2+1)
        if all([(((x in q) and not(x in a)) and ((x in a) or not(x in p))) == False for x in range(1,100*k)]):
            if a2 - a1 < a2_best - a1_best:
                a1_best = a1
                a2_best = a2

print(a1_best/k,a2_best/k,(a2_best-a1_best)/k)
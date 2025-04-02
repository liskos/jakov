k = 10
p = range(130*k,171*k+1)
q = range(150*k,185*k+1)

a1_best = 0
a2_best = 500
for a1 in range(146*k,153*k+1):
    for a2 in range(169*k,174*k+1):
        a = range(a1,a2+1)
        if all([not(x in p) or (not((x in q) and (x not in a)) or (x not in p)) for x in range(1,200*k)]):
            if a2 - a1 < a2_best - a1_best:
                a2_best = a2
                a1_best = a1


print(a1_best/k,a2_best/k,(a2_best-a1_best)/k)
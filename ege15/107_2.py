p = set(range(12,26+1))
q = set(range(30,53+1))
a1_best = 0
a2_best = 0
for a1 in range(10,100):
    for a2 in range(a1,250):
        a = range(a1,a2+1)
        if all([(not(x in a) or (x in p)) or (x in q) for x in range(1,500)]):
            if a2 - a1 > a2_best - a1_best:
                a2_best = a2
                a1_best = a1
print(a1_best,a2_best,a2_best-a1_best)

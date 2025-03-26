
p = range(25,50+1)
q = range(32,47+1)

a1_best = 0
a2_best = 0
for a1 in range(22,57+1):
    for a2 in range(28,55+1):
        a = range(a1,a2+1)
        if all([not(not(x in a) or not(x in p)) or(not(x in a) or (x in q)) for x in range(1,100)]):
            if a2 - a1 > a2_best - a1_best:
                a2_best = a2
                a1_best = a1
print(a1_best,a2_best,(a2_best - a1_best))
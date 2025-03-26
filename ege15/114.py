
p = range(25,37+1)
q = range(32,50+1)

a1_best = 0
a2_best = 0
for a1 in range(21,42+1):
    for a2 in range(27,55+1):
        a = range(a1,a2+1)
        if all([not((x in a) and not (x in q)) or ((x in p)or(x in q)) for x in range(1,100)]):
            if a2 - a1 > a2_best - a1_best:
                a1_best = a1
                a2_best = a2
print(a1_best,a2_best,(a2_best-a1_best))
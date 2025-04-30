k = 10
c = range(48*k,94*k+1)
j = range(83*k,100*k+1)
a1_best = 0
a2_best = 0
for a1 in range(45*k,53*k+1):
    for a2 in range(97*k,104*k+1):
        a = range(a1,a2+1)
        if all([((x in c) or (x in j)) or not(x in a) for x in range(1,140*k)]):
            if a2 - a1 > a2_best - a1_best:
                a1_best = a1
                a2_best = a2


print(a1_best/k,a2_best/k,(a2_best-a1_best)/k)

#52
k = 30
p = range(5*k,30*k+1)
q = range(14 * k,23 * k + 1)

a1_best = 0
a2_best = 0
for a1 in range(3*k,8*k+1):
    for a2 in range(12*k,14*k+1):
        a = range(a1,a2+1)
        if all([(not((x in p)==(x in q))) or not(x in a) for x in range(1,100*k)]):
            if a2 - a1 > a2_best - a1_best:
                a2_best = a2
                a1_best = a1
print(a1_best/k, a2_best/k, (a2_best-a1_best)/k)
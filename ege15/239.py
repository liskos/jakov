k = 1
d = range(155*k,177*k+1)
b = range(111*k,130*k+1)

a1_best = 0
a2_best = 500
for a1 in range(1*k,200*k+1):
    for a2 in range(a1*k,200*k+1):
        a = range(a1,a2+1)
        if all([not(x in d) or (not(not(x in b) and not(x in a)) or not(x in d)) for x in range(1,200*k)]):
            if a2 - a1 < a2_best - a1_best:
                a2_best = a2
                a1_best = a1


print(a1_best/k,a2_best/k,(a2_best-a1_best)/k)
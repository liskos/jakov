k = 10
p = (range(44*k,49*k+1))
q = (range(28*k,53*k+1))


a1_best = 0
a2_best = 0
for a1 in range(14*k,52*k):
    for a2 in range(26*k,60*k):
        a = range(a1,a2+1)
        if all([(not(x in a) or (x in p)) or (x in q) for x in range(1,100*k)]):
            if a2 - a1 > a2_best - a1_best:
                a2_best = a2
                a1_best = a1
print(a1_best,a2_best,(a2_best-a1_best)/k)

# p = set(range(44,49+1))
# q = set(range(28,53+1))
# a1_best = 0
# a2_best = 0
# for a1 in range(14,100):
#     for a2 in range(a1,250):
#         a = range(a1,a2+1)
#         if all([(not(x in a) or (x in p)) or (x in q) for x in range(1,500)]):
#             if a2 - a1 > a2_best - a1_best:
#                 a2_best = a2
#                 a1_best = a1
# print(a1_best,a2_best,a2_best-a1_best)

a = set()
p = {2,4,6,8,10,12,14,16,18,20}
q = {3,6,9,12,15,18,21,24,27,30}

for i in range(1,100):
    a.add(i)
    if not all([(not(x in a) or not(x in p)) and ((x in q) or not(x in a)) for x in range(1,100)]):
        a.remove(i)


print(len(a),a)
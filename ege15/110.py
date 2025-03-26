a = set()
p = {2,4,6,8,10,12,14,16,18,20}
q = {5,10,15,20,25,30,35,40,45,50}

for i in range(1,100):
    a.add(i)
    if not all([(not(x in a) or (x in p)) and (not(x in q) or not(x in a)) for x in range(1,100)]):
        a.remove(i)
print(len(a),a)
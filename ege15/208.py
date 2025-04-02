b = set()
for a in range(1,500):
    if all([(not(not(x & a != 0) or (x & 62 != 0)) or((x & 24 == 0) and (x & a != 0))) == False for x in range(1,500)]):
        b.add(a)

print(b)
b = set()
for a in range(1,500):
    if all([(not(not(x & 7 != 0) or (not(x & a != 0) or (x & 54 != 0))) or ((x & 27 == 0) and (x & a != 0) and (x & 7 != 0))) == False for x in range(1,500)]):
        b.add(a)

print(b)
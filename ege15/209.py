b = set()
for a in range(43,56):
    if all([(not(not(x & 17 != 0) or (not(x & a != 0) or (x & 58 != 0))) or ((x & 8 == 0) and (x & a != 0) and (x & 58 == 0))) == False  for x in range(1,500)]):
        b.add(a)

print(b)
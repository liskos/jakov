a = set(range(1,100))
for i in range(1,100):
    a.remove(i)
    if not all([(x in a) or (not(x in {1,12}) and not(x in {12,13,14,15,16})) for x in range(1,100)]):
        a.add(i)


print(a)
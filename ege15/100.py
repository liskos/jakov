a = set(range(1,100))
for i in range(1,100):
    a.remove(i)
    if not all([(x in a) or not(x in {1,3,7}) or (not(x in {1,2,4,5,6}) and (x in {1,3,7})) for x in range(1,100)]):
        a.add(i)
print(a)
a = set(range(1,100))
for i in range(1,100):
    a.remove(i)
    if not all([not(not(x in a) and (x in {3,6,9,12})) or not(x in {1,2,3,4,5,6}) for x in range(1,101)]):
        a.add(i)

print(len(a))
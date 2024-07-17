a = {3}
for i in range(12):
    b = set()
    for x in a:
        b.add(x+1)
        b.add(x*2-3)
    a = b.copy()
print(len(a))
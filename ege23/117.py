a = {1}
for i in range(7):
    b = set()
    for x in a:
        b.add(x+1)
        b.add(x+5)
        b.add(x*3)
    a = b.copy()
print(len(a))

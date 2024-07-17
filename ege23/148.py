a = {2}
for i in range(13):
    b = set()
    for x in a:
        b.add(x+3)
        b.add(x*2+1)
    a = b.copy()
print(len(a))
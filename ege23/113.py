a = {1}
for i in range(1000):
    b = set()
    for x in a:
        b.add(x+1)
        b.add(x+5)
        b.add(x*3)
    a = b.copy()
    if 227 in a:
        print(i+1)
        break



a = {1}
for i in range(8):
    b = set()
    for x in a:
        b.add(x+1)
        b.add(x+5)
        b.add(x*3)
    a = b.copy()

f = 0
for n in a:
    if 1000 <= n <= 1024:
        f+=1
print(f)
print(len([n for n in a if 1000 <= n <= 1024]))

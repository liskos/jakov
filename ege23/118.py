a = {1}
for i in range(6):
    b = set()
    for x in a:
        b.add(x+1)
        b.add(x+2)
        b.add(x*2)
    a = b.copy()
f = 0
for n in a:
    if 34 <= n <= 59:
        f+=1
print(f)
f = [n for n in a if 34<= n <= 59]
print(len(f))
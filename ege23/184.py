a = {133}
for i in range(9):
    b = set()
    for x in a:
        b.add(x - 3)
        b.add(x * (- 3))
    a = b.copy()
k = 0
for x in a:
    if x > 0:
        k+=1
print(k)


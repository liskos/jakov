a = {133}
for i in range(9):
    b = set()
    for x in a:
        b.add(x - 3)
        b.add(x * - 3)
    a = b.copy()
print(len(set(a)))



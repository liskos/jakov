p = 0
b = []
c = []
for n in range(33333,55555+1):
    a = [str(int(i) % 2) for i in str(n)]
    a = "".join(a)
    if a == "11010":
        b.append(n)

for n in b:
    if n % 6 != 0 and n % 7 != 0 and n % 8 != 0:
        c.append(n)

print(len(c),max(c)-min(c))


# 2346 22092

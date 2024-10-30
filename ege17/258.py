a = [int(x) for x in open("17data/17-257.txt")]
r = []
b = []
n = []
for x in range(len(a)):
    if a[x] % 2 == 0:
        b.append(a[x])
    if a[x] % 2 != 0:
        n.append(a[x])

for i in range(len(a) - 1):
    if max(b) > max(n):
        r = b
    else:
        r = n

print(len(r), min(r))
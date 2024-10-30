a = [int(x) for x in open("17data/17-257.txt")]
r = []
b = []
n = []
for x in range(len(a)):
    if a[x] % 7 == 0:
        b.append(a[x])
    if a[x] % 13 == 0:
        n.append(a[x])

for i in range(len(a) - 1):
    if min(b) > min(n):
        r = b
    else:
        r = n

print(len(r), max(r))
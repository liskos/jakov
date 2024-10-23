a = [int(x) for x in open("17data/17-4.txt")]
r = []
for i in range(len(a)):

    if str(a[i])[-1] in "57" and a[i] % 9 != 0 and a[i] % 11 != 0:
        r.append(a[i])
print(len(r),(max(r)+min(r)))
a = [int(x) for x in open("17 (1).txt")]
r = []
b = []
for x in range(len(a)):
    if a[x] % 2042 == 0:
        b.append(a[x])

for i in range(len(a)-1):
    if (a[i]+a[i+1]) > len(b):
        r.append(a[i]+a[i+1])

print(len(r),max(r))
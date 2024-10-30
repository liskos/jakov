a = [int(x) for x in open("17data/17-257.txt")]
r = []
b = []

for x in range(len(a)):
    if (str(a[x]))[-1] == "4":
        b.append(a[x])

n = max(b) + min(b)
for i in range(len(a) - 1):
    if (a[i] + a[i+1]) < n:
        r.append(a[i]+a[i+1])


print(len(r), max(r))
a = [int(x) for x in open("17data/17-1.txt")]
r = []

av = sum(a) / len(a)
for i in range(len(a) - 2):
    tr = a[i:i+3]
    if ((a[i] < av) or (a[i+1] < av) or (a[i+2] < av)) and sum(1 for x in tr if x % 7 == 0) >= 2:
        r.append(a[i] + a[i+1] + a[i+2])

print(len(r), max(r))
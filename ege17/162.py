a = [int(x) for x in open("17data/17-3.txt")]
r = []

for i in range(len(a)-1):
    if ((a[i] * a[i+1]) % 2 != 0) and (((a[i] + a[i+1]) / 2) % 7 == 0):
        r.append((a[i] + a[i+1])/2)
print(len(r),min(r))
a = [int(x) for x in open("17data/17-3.txt")]
r = []

for i in range(len(a)-1):
    if (a[i] % 2 == 0 and a[i] % 4 == 0 and a[i+1] % 2 != 0 and a[i+1] % 11 == 0) or (a[i] % 2 != 0 and a[i] % 11 == 0 and a[i+1] % 2 == 0 and a[i+1] % 4 == 0):
        r.append(a[i] + a[i+1])

print(len(r),max(r))
a = [int(x) for x in open("17data/17-4.txt")]
r = []

for i in range(len(a)):
    if str(a[i])[-1] == "2" and a[i] % 3 == 0 and a[i] % 11 == 0:
        r.append(a[i])
    elif str(a[i])[-1] == "7" and a[i] % 3 == 0 and a[i] % 11 == 0:
        r.append(a[i])

print(len(r),min(r))
a = [int(x) for x in open("17data/17-4.txt")]
r = []
for i in range(len(a)):

    if abs(a[i]) % 13 == 7 and a[i] % 7 != 0 and a[i] % 11 != 0:
        r.append(a[i])
print((max(r)-min(r)),len(r))
a = [int(x) for x in open("17data/17-4.txt")]
r = []
for i in range(len(a)):

    if  abs(a[i]) % 100 < 50 and abs(a[i]) % 1000 > 299 and abs(a[i]) % 1000 < 800:
        r.append(a[i])
print(len(r),min(r))
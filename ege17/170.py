a = [int(x) for x in open("17data/17-4.txt")]
r = []
for i in range(len(a)):

    if  abs(a[i]) % 13 == 4 and abs(a[i]) % 8 == 1:
        r.append(a[i])
print(max(r),sum(r))
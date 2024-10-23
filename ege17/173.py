a = [int(x) for x in open("17data/17-4.txt")]
r = []
for i in range(len(a)):

    if  a[i] % 3 == 0 and a[i] % 9 != 0 and abs(a[i]) % 10 > 3:
        r.append(a[i])
print(len(r),sum(r)/len(r))

a = [int(x) for x in open("17data/17-1.txt")]
r = []
for i in range(len(a) - 1):

    if (a[i] % 9 == 0 and abs(a[i+1]) % 8 == 3 and a[i+1] % 9 != 0) or (abs(a[i]) % 8 == 3 and a[i] % 9 != 0 and a[i + 1] % 9 == 0):
        r.append(max(a[i],a[i + 1]))
print(len(r),max(r))
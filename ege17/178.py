a = [int(x) for x in open("17data/17-4.txt")]
r = []
p = [2,3]
v = [5,7]
for i in range(len(a)):
        if (a[i] % p[0] == 0 and a[i] % p[1] == 0)
        r.append(a[i])
print(max(r),len(r))
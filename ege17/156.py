a = [int(x) for x in open("17data/17-2.txt")]
r = []
for i in range(len(a)-1):
    if (max(a) == a[i]):
     r.append(a[i])
print(len(r),a.index(max(a)),r,a)
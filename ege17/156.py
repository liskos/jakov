a = [int(x) for x in open("17data/17-2.txt")]
r = []
m = max(a)
for i in range(len(a)-1):
    if (m == a[i]):
     r.append(i)
print(len(r),r[0]+1)
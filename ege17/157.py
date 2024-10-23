a = [int(x) for x in open("17data/17-2.txt")]
r = []
b = min(a)
for i in range(len(a)-1):
    if b == a[i]:
        r.append(i)
print(len(r),r[-1]+1,r)
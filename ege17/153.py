a = [int(x) for x in open("17data/17-1.txt")]
r = []
for i in range(len(a)-1):
    if (a[i] < a[i+1]):
     r.append(abs(a[i] - a[i+1]))
print(len(r),min(r),r)
a = [int(x) for x in open("17data/17-333.txt")]
r = []
b = list(a)
d = [x for x in a if len(str(x))==4]
print(d)

for i in range(len(a)-1):
    if b.count(a[i] + a[i+1]) == 0 and (a[i] + a[i+1]) < sum(d)/len(d):
        r.append(a[i]+a[i+1])
print(len(r),max(r))

a = [int(x) for x in open("17data/17-302.txt")]
r = []
b = []
for x in range(len(a)):
    if a[x] % 21 == 0:
        b.append(a[x])
def f(x,v):
    return abs(((x+v)/2)-min(b))**0.5 == int(abs(((x+v)/2)-min(b))**0.5)

for i in range(len(a)-1):
    if f(a[i],a[i+1]):
        r.append(a[i]*a[i+1])
print(len(r),min(r))

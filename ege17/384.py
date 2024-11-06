a = [int(x) for x in open("17data/17-384.txt")]
r = []
b = []
def f(x):
    return len(str(x)) == 2
for x in range(len(a)-1):
    if f(a[x]) != f(a[x+1]):
        b.append(a[x]+a[x+1])



for i in range(len(a)-1):
    if a[i]+a[i+1] > max(b):
        r.append(min(a[i],a[i+1]))

print(len(r),min(r))
a = [int(x) for x in open("17data/17-342.txt")]
r = []
b = min(x for x in a if x % 37 == 0)
d = max(x for x in a if x % 73 == 0)



def f(x):
    return b < x < d

for i in range(len(a)-1):
    if f(a[i]) != f(a[i+1]):
        r.append(a[i]+a[i+1])

print(len(r),min(r))
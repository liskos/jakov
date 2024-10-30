a = [int(x) for x in open("17data/17-272.txt")]
r = []
b = []



def d(a,b):
    return (a % 10 + b % 10) == 7
for i in range(len(a)-1):
    if d(a[i],a[i+1]):
        r.append(a[i]+a[i+1])
def f(x):
    return x < (sum(r)/len(r))
for i in range(len(a)-1):
    if f(a[i]) and f(a[i+1]) and d(a[i],a[i+1]):
        b.append(a[i]+a[i+1])
print(len(r),max(b))
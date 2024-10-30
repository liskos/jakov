a = [int(x) for x in open("17data/17-243.txt")]
r = []
b = []

for x in range(len(a)):
    if a[x] % 49 == 0:
        b.append(sum(map(int,str(a[x]))))

def f(x):
    return x > sum(b)
def d(x):
    return x % 10 == 7
for i in range(len(a)-1):
    if f(a[i]) != d(a[i]) and f(a[i+1]) != d(a[i+1]):
        r.append(a[i]+a[i+1])

print(len(r),max(r))
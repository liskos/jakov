a = [int(x) for x in open("17data/17-272.txt")]
r = []
b = []
c = []
for x in range(len(a)):
    if a[x] > 0:
        b.append(a[x])
def summ(x):
    return sum(map(int,str(abs(x))))
def f(x):
    return x > (sum(b)/len(b))
for i in range(len(a)-1):
    if f(a[i]) or f(a[i+1]):
        r.append(a[i]+a[i+1])

for i in range(len(a)-1):
    if f(a[i]) or f(a[i+1]):
        c.append(max(summ(a[i]),summ(a[i+1])))
print(len(r),max(c))
a = [int(x) for x in open("17data/17-324.txt")]
r = []
b = []
for x in range(len(a)):
    if a[x] % 37 != 0:
        b.append(a[x])

def f(x, v, c):
    n = x + v + c
    return bin(n)[2:] == (bin(n)[2:])[::-1]


for i in range(len(a) - 2):
    if f(a[i],a[i+1],a[i+2]) and (min(a[i],a[i+1],a[i+2]) > sum(b)/len(b)):
        r.append(a[i]+a[i+1]+a[i+2])

print(len(r),max(r))
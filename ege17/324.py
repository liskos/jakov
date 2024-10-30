a = [int(x) for x in open("17data/17-324.txt")]
r = []
b = []
for x in range(len(a)):
    if a[x] % 11 == 0:
        b.append(a[x])

def f(x, v, c):
    n = x + v + c
    s = ""
    t = "0123456"
    while n > 0:
        s = t[n%7] + s
        n //= 7
    return s == s[::-1]

for i in range(len(a) - 2):
    if f(a[i],a[i+1],a[i+2]) and (a[i] + a[i+1] + a[i+2]) / 3 < sum(b)/len(b):
        r.append(a[i]+a[i+1]+a[i+2])

print(len(r),min(r))
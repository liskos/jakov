a = [int(x) for x in open("17data/17-324.txt")]
r = []
b = []
for x in range(len(a)):
    if a[x] % 31 == 0:
        b.append(a[x])

def f(x, v, c):
    n = x + v + c
    s = ""
    t = "01234"
    while n > 0:
        s = t[n%5] + s
        n //= 5
    return s == s[::-1]

for i in range(len(a) - 2):
    if f(a[i],a[i+1],a[i+2]) and (a[i] + a[i+1] + a[i+2]) / 3 > sum(b)/len(b):
        r.append(a[i]+a[i+1]+a[i+2])

print(len(r),min(r))
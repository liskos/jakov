a = [int(x) for x in open("17data/17-282.txt")]
r = []
b = []

for x in range(len(a)):
    if a[x] % 11 == 0:
        b.append(a[x])
def tr(n):
    s = ""
    t = "012"
    while n > 0:
        s = t[n%3]+s
        n //= 3
    return s

def f(x):
    return sum(map(int,(tr(x)))) == sum(map(int,(tr(max(b)))))

for i in range(len(a)-1):
    if f(a[i]) or f(a[i+1]):
        r.append(a[i]+a[i+1])

print(len(r),min(r))
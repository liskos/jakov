def vos(n):
    n = abs(n)
    t = "01234567"
    s = ""
    while n > 0:
        s = t[n%8] + s
        n //= 8
    return s


a = [int(x) for x in open("17data/17-1.txt")]
r = []
for i in range(len(a) - 1):
    b = vos(a[i + 1])[-1]
    d = vos(a[i])[-1]
    if (a[i] % 9 == 0 and b == "3") or (d == "3" and a[i + 1] % 9 == 0):
        r.append(a[i] + a[i + 1])
print(len(r),min(r))
def tr(n):
    t = "012"
    s = ""
    while n > 0:
        s = t[n%3] + s
        n //= 3
    return s
def pr(n):
    t = "01234"
    s = ""
    while n > 0:
        s = t[n % 5] + s
        n //= 5
    return s

a = [int(x) for x in open("17data/17-4.txt")]
r = []
for i in range(len(a)):

    if tr(abs(a[i]))[-1] == pr(abs(a[i]))[-1] and (a[i] % 31 == 0 or a[i] % 47 == 0 or a[i] % 53 == 0):
        r.append(a[i])
print(len(r),min(r))
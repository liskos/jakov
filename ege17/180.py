a = [int(x) for x in open("17data/17-4.txt")]
r = []
def pr(n):
    t = "01234"
    s = ""
    while n > 0:
        s = t[n%5] + s
        n //= 5
    return s
def dev(n):
    t = "012345678"
    s = ""
    while n > 0:
        s = t[n%9] + s
        n //= 9
    return s

for i in range(len(a)):
    if pr(a[i])[-1] == "3" and dev(a[i])[-1] == "5" and (oct(a[i])[2:])[-1] != "7":
        r.append(a[i])
print(len(r),max(r))
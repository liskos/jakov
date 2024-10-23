a = [int(x) for x in open("17data/17-7.txt")]
r = []
def tr(n):
    t = "012"
    s = ""
    while n > 0:
        s = t[n%3] + s
        n //= 3
    return s

for i in range(len(a)-2):
    if tr(a[i])[0] == "2" or tr(a[i+1])[0] == "2" or tr(a[i+2])[0] == "2":
        r.append(a[i]+a[i+1]+a[i+2])
print(len(r),min(r))
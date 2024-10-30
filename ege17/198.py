a = [int(x) for x in open("17data/17-10.txt")]
r = []

def sem(n):
    t = "0123456"
    s = ""
    while n > 0:
        s = t[n%7] + s
        n //= 7
    return s

for i in range(len(a)-1):
    if sem((a[i] + a[i+1])) == sem((a[i] + a[i+1]))[::-1]:
        r.append((a[i] + a[i+1]))

print(len(r),sem(max(r)))
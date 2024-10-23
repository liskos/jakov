a = [int(x) for x in open("17data/17-4.txt")]
r = []
def pr(n):
    t = "01234"
    s = ""
    while n > 0:
        s = t[n % 5] + s
        n //= 5
    return s

for i in range(len(a)):

    if (bin(a[i])[2:])[-4:] == "1001" and pr(a[i])[-2:] == "11":
        r.append(a[i])

print(max(r),sum(r))
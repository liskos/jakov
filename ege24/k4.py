s = open("kege/24.5_19717.txt").read()

m = 0
k = 0
l = 0
for r in range(len(s)):
    if s[r] == "M":
        k += 1
    while k > 278:
        if s[l] == "M":
            k -= 1
        l += 1
    if k <= 278:
        m = max(m,r-l+1)


print(m)
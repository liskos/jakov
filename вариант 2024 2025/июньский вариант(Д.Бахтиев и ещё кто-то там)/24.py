s = open("24_22446.txt").read()
k = 0
l = 0
m = 0
for r in range(len(s)):
    if s[r:r+3] == "LND":
        k += 1
    while k >= 10000 :
        if s[l:l+3] == "LND":
            k -= 1
        l += 1
    l2 = l
    while s[l2] != s[r+2] and l2 < r+2:
        l2 += 1
    if k <= 10000:
        m = max(m,r-l+3)

print(m)
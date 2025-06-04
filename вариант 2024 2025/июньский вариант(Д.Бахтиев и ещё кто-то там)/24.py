s = open("24_22446.txt").read()
k = 0
l = 0
m = 0
for r in range(len(s)):
    if s[r:r+3] == "LND":
        k += 1
        while k >= 10000 or s[l] != s[r]:
            if s[l:l+3] == "LND":
                k -= 1
            l += 1
    if k <= 10000 and s[l] == s[r]:
        m = max(m,r-l+2)

print(m)
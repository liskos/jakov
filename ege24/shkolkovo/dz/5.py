s = open("files/24_13715__3kjzr (1).txt").read()
k = 0
l = 0
m = 0
for r in range(len(s)):
    if s[r:r+2] == "CD":
        k += 1
    while k > 50:
        if s[l:l+2] == "CD":
            k -= 1
        l += 1
    if k == 50:
        m = max(m,r-l+2)

print(m)
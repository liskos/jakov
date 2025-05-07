s = open("kege/24_21717 (1).txt").read()

k = 0
m = 100000
l = 0
for r in range(len(s)):
    if s[r:r+3] == "RSQ":
        k += 1
    while k > 130 or s[l] == "Q":
        if s[l:l+3] == "RSQ":
            k -= 1
        l += 1
    if k == 130:
        m = min(m,r-l+3)

print(m,s[l:r+1])
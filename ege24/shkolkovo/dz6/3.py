s = open("24_M3__42ngp.txt").read()
t = 0
gl = 0
l = 0
m = 0
import string
for r in range(len(s)):
    if s[r] == ".":
        t += 4
    if s[r] in "AEIOUY":
        gl += 1
    while t > 6:
        if s[l] == ".":
            t -= 1
        l += 1
    if gl > 15:
        m = max(m,r-l+1)


print(m)
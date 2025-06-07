s = open("files/24_M3__42nfh.txt").read()
# abcdefghijklmnopqrstuvwxyz
m = 0
k = 0
l = 0
t = 0
for r in range(len(s)):
    if s[r] == ".":
        t += 1
    if s[r] in "AEIOUY":
        k += 1
    while t > 6:
        if s[l] == ".":
            t -= 1
        if s[l] in "AEIOUY":
            k -= 1
        l += 1
    if t < 7 and k > 15:
        m = max(m,r-l+1)

print(m)
s = open("24data/24-280.txt").read()

m = 0
l = 0
for r in range(len(s)):
    while s[r] in s[l:r]:
        l += 1
    m = max(m,r-l+1)
print(m)
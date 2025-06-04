s = open("24_18562.txt").read()

l = 0
m = 0
for r in range(len(s)):
    while "XYYYZ" in s[l:r+1]:
        l += 1
    m = max(m, r-l +1)
print(m)
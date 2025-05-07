s = open("kege/24_19254.txt").read()

m = 0
l = 0
k = 0

for r in range(len(s)):
    if s[r:r+4] == "FSRQ":
        k += 1
        while k > 80:
            if s[l:l+4] == "FSRQ":
                k -= 1
            l += 1
    if k == 80:
        m = max(m,r-l+4)


print(m)
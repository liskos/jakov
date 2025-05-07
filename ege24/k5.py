s = open("kege/24_19254.txt").read()

m = 0
l = 0
k = 0

for r in range(len(s)):
    if s[r:r+3] == "WWF":
        k += 1
        while k > 120 or s[l:r+3] == "WSFWW":
            if s[l:l+3] == "WWF":
                k -= 1
            l += 1
    if k <= 120:
        m = max(m,r-l+3)


print(m)
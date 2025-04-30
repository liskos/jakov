s = open("24data/24-280.txt").read()

m = 0
ind = [i+1 for i in range(len(s)-1) if s[i] == "X" or s[i] == "Y"]
for l in ind:
    x = 0
    y = 0
    for r in range(l,len(s)):
        if s[r] == "X": x += 1
        if s[r] == "Y": y += 1
        if x > 1 or y > 1: break
        if x == 1 and y == 1: m = max(m,r-l+1)

print(m)
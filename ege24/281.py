s = open("24data/24-280.txt").read()

m = 0
ind = [i+1 for i in range(len(s)-1) if s[i] == "X" or s[i] == "Y" or s[i] == "Z"]
for l in ind:
    x = 0
    y = 0
    z = 0
    for r in range(l,len(s)):
        if s[r] == "X": x += 1
        if s[r] == "Y": y += 1
        if s[r] == "Z": z += 1
        if x > 5 or y > 5 or z > 5: break
        if x == 5 and y == 5 and z == 5: m = max(m,r-l+1)

print(m)
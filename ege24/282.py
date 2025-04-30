s = open("24data/24-280.txt").read()

m = 0
ind = [i+1 for i in range(len(s)-1) if s[i] == "A" or s[i] == "E" or s[i] == "I"
       or s[i] == "O" or s[i] == "U" or s[i] == "Y"]
for l in ind:
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    y = 0
    for r in range(l,len(s)):
        if s[r] == "A": a += 1
        if s[r] == "E": e += 1
        if s[r] == "I": i += 1
        if s[r] == "O": o += 1
        if s[r] == "U": u += 1
        if s[r] == "Y": y += 1

        if a > 8 or e > 8 or i > 8 or o > 8 or u > 8 or y > 8: break
        if a == 8 and e == 8 and i == 8 and o == 8 and u == 8 and y == 8: m = max(m,r-l+1)

print(m)
s = open("24data/24-280.txt").read()

m = 0
l = 0
x = 0
y = 0
for r in range(len(s)):
    if s[r] == "X":x += 1
    if s[r] == "Y":y += 1
    while x > 5 or y > 5:
        if s[l] == "X": x -= 1
        if s[l] == "Y": y -= 1
        l += 1
    if x <= 5 and y <= 5:
        m = max(m, r-l+1)

print(m)




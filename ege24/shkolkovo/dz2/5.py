s = open("files/24_18__3b9tx.txt").read()
f = 0
l = 0
ld = 0
m = 0
for r in range(len(s)):
    if s[r] == "F":
        f += 1
    if s[r] == "L":
        ld += 1
    while f > 3 or ld > 3:
        if s[l] == "L":
            ld -= 1
        if s[l] == "F":
            f -= 1
        l += 1
    m = max(m,r-l+1)
print(m)
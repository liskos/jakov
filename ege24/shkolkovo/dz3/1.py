s = open("files/24__3ns0t.txt").read()

m = 0
k = 0
l = 0
for r in range(len(s)):
    if s[r] == "B":
        k += 1
    while k > 53:
        if s[l] == "B":
            k -= 1
        l += 1
    if k == 53:
        m = max(m,r-l+1)

print(m)
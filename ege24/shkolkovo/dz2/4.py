s = open("files/24_16__3b9u2.txt").read()

l = 0
m = 1000
k = 0
for r in range(len(s)):
    if s[r] == "Y":
        k += 1
    while k > 100:
        if s[l] == "Y":
            k -= 1
        l += 1
    if k >= 100:
        m = min(m,r-l+1)
print(m)
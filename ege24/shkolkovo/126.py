s = open("files/24_4__3b9tg.txt").read()

m = 0
k = 0
l = 0
for r in range(len(s)):
    if s[r] == "D":
        k += 1
        while k > 100:
            if s[l] == "D":
                k -= 1
            l += 1
    m = max(m,r-l+1)

print(m)
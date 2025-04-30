s = open("24data/24-295.txt").read()
l = 0
m = 0
k = 0
for r in range(len(s)):
    if s[r:r+2] == "DE":
        k += 1

    while k > 240:
        if s[l:l+2] == 'DE':
            k -= 1
        l += 1
    m = max(m,r-l+2)

print(m)
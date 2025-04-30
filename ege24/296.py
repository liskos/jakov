s = open("24data/24-296.txt").read()

m = 0
l = 0
k = 0

for i in range(len(s)):
    if s[i:i+2] == "CD":
        k += 1
    while k > 160:
        if s[l:l+2] == "CD": k -= 1
        l += 1
    if k == 160:
        m = max(m,i-l+1)

print(m)
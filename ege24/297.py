s = open("24data/24-296.txt").read()

l = 0
m = 10000
k = 0
for i in range(len(s)):
    if s[i:i+2] == "AF":
        k += 1
    while k > 201:
        if s[l:l+2] == "AF":
            k -= 1
        l += 1
    if k > 200:
        m = min(m,i-l+1)


print(m)

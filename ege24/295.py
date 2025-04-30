s = open("24data/24-295.txt").read()
l = 0
m = 0
k = 0
for i in range(len(s)):
    if s[i:i+2] == "DE":
        k += 1

    while k > 240:
        if s[l:l+2] == 'DE':
            k -= 1
        l += 1
    m = max(m,i-l+1)

print(m)
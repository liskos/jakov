s = open("24data/24-309.txt").read()

l = 0
t = ""
m = 0
k = 0
for i in range(len(s)):
    if s[i:i+4] == "FSRQ":
        k += 1
    while k > 80:
        if s[l:l+4] == "FSRQ":
            k -= 1
        l += 1
    if k == 80:
        m = max(m,i-l+1)
print(m)
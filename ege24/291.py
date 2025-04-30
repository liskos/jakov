s = open("24data/24-280.txt").read()

m = 0
t = ""
for i in range(len(s)):
    if t.count(s[i]) == 0:
        t += s[i]
    else:
        t = s[i]
    m = max(m,len(t))


print(m)
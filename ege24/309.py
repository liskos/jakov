s = open("24data/24-309.txt").read()


t = ""
m = 0

for i in range(len(s)):
    if t and t.count("FSRQ") == 80:
        m = max(m,len(t))
    elif t and t.count("FSRQ") < 80:
        t += s[i]
    else:
        t = s[i]


print(m)
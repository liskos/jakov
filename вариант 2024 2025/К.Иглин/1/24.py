s = open("24_18562.txt").read()

t = ""
m = 0
for i in range(len(s)):
    if t and (t + s[i]).count("XYYYZ") == 0:
        t += s[i]
        m = max(m,len(t)+1)
    else:
        t = s[i]
m = max(m,len(t))

print(m)
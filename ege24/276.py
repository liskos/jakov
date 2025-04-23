s = open("24data/24-276.txt").read()

t = ""
m = 0
for i in range(len(s)):
    if len(t) > 1 and t[0] in "13579" and t[-1] == t[0] and t.count(t[0]) == 2:
        m = max(m,len(t))
        t = s[i]
    elif t and t[0] in "13579" and (s[i] == "F" or s[i] == t[0]):
        t += s[i]
    else:
        t = s[i]

print(m)
s = open("24data/24-278.txt").read()
m = 0
t = ""

for i in range(len(s)):
    if t and len(t) > 1 and t[-1] == t[0] and t.count(t[0]) == 2:
        m = max(len(t),m)
    elif t and t[0] in "02468" and ((s[i] == t[0]) or (s[i] in "KNLF")):
        t += s[i]
    else:
        t = s[i]


print(m)
s = open("24data/24-264.txt").read()

t = ""
m = 0
for i in range(len(s)):
    if t and t[-1].isdigit() != s[i].isdigit():
        t += s[i]
        m = max(m,len(t))
    else:
        t = s[i]


print(m)
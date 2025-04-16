s = open("24data/24-j6.txt").read()

b = []
t = ""
for i in range(len(s)):
    if t and t[-1] < s[i]:
        t += s[i]
    else:
        b.append(t)
        t = s[i]


print(len([x for x in b if len(x) > 4 and len(x) < 6]))
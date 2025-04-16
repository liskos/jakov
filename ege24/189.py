s = open("24data/24-181.txt").read()

t = ""
maxlen = 0

for i in range(len(s)):
    if t == "":
        t = s[i]
    elif t.count(".") == 0 and t.count("Y") + t.count("A") + t.count("E") + t.count("I") + t.count("O") + t.count("U") < 8:
        t += s[i]
    else:
        t = s[i]
    if len(t) > maxlen:
        maxlen = len(t)


print(maxlen)
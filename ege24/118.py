s = open("24data/24.txt").read()

t = ""
maxlen = 0
index = 0

for i in range(len(s)):
    if t == "":
        t = s[i]
    elif t[-1] > s[i]:
        t += s[i]
    else:
        t = s[i]

    if len(t) > maxlen:
        maxlen = len(t)
        index = i - len(t) + 1


print(index)
s = open("24data/24-181.txt").read()

t = ""
maxlen = 0
k = 0
for i in range(len(s)):
    if s[i] == ".":
        k += 1
    t += s[i]
    while k > 1:
        if t[0] == ".":
            k -=1
        t = t[1:]
    if len(t) > maxlen:
        maxlen = len(t)


print(maxlen)
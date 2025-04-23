s = open("24data/24-181.txt").read()

t = ""
maxlen = 0
k = 0
for i in range(len(s)):
    if s[i] == ".":
        k += 1
        t += s[i]
    elif s[i] in "AEIOUY":
        t = ""
        k = 0
    else:
        t += s[i]
    if len(t) > maxlen and k >= 6:
        maxlen = len(t)



print(maxlen)
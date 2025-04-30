s = open("ycheba/24_14__3b9u9.txt").read()

t = ""
m = 0
for i in range(len(s)):
    if t and ((t[-1] + s[i] not in "TT") and (t[-1] + s[i]) not in "VV"):
        t += s[i]
    else:
        t = s[i]
    m = max(m,len(t))

print(m)
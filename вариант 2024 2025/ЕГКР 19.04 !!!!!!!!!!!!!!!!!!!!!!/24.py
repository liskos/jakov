s = open("24_21717.txt").read()

m = 100000
l = 0
k = 0
t = ""
for i in range(len(s)):
    if t.count("RSQ") == 130 and t[-1] != "Q":
        m = min(m,len(t))
        break
    t += s[i]

print(m)
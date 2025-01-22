s = open("24.txt").read()
m = 0
t = ""
for i in s:
    t += i
    while t.count("FE") > 200:
        t = t[1:]
    if t.count("FE") == 200:
        m = max(m,len(t))
print(m)
s = open("24data/24-280.txt").read()

t = ""
m = 0

for i in range(len(s)):
    if t and t.count("X") == 1 and t.count("Y") == 1:
        m = max(m,len(t))
        t = s[i]
    elif t and t.count("Y") < 2 and t.count("X") < 2:
        t += s[i]
        print(t)
    else:
        t = s[i]


print(m)
s = open("24data/24-280.txt").read()

t = ""
m = 0

for i in range(len(s)):
    if t.count("X") == 5 and t.count("Y") == 5 and t.count("Z") == 5:
        m = max(len(t),m)
        t = s[i]
    elif t and ((t.count("X") == 4 or t.count("Y") == 4 or t.count("Z") == 4) or (t.count("X") < 4 or t.count("Y") < 4 or t.count("Y") < 4)):
        t += s[i]

    else:
        t = s[i]


print(m)
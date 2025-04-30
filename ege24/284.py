s = open("24data/24-280.txt").read()

t = ""
m = 0


for i in range(len(s)):
    if t.count("X") + t.count("Y") < 6:
        t += s[i]
        while t.count("X") + t.count("Y") > 5:
            if t[0] == "Y" or t[0] == "X":
                t = t[1:]
            t = t[1:]
    if t.count("X") + t.count("Y") < 6:
        m = max(m,len(t))



print(m)
s = open("24data/24-280.txt").read()

t = ""
m = 0


for i in range(len(s)):
    if t.count("X") < 1 or t.count("Y") < 1 and t.count("A") == 0:
        t += s[i]
        while t.count("X") > 1 or t.count("Y") == 1 or t.count("A") > 0:
            if t[0] == "Y" or t[0] == "X" or t[0] == "A":
                t = t[1:]
            t = t[1:]
    if t.count("X") == 1 or t.count("Y") == 1 and t.count("A") == 0:
        m = max(m,len(t))



print(m)
s = open("files/24-280__6eq3c.txt").read()
m = 0
t = ""
for i in s:
    if t and i != "D" and i not in "CD":
        t += i
    elif t and i == "D":
        t += i
        m = max(m,len(t))
        t = ""
    elif i == "C":
        t = i

print(m)
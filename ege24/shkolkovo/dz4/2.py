s = open("files/24-280__6eq3c .txt").read()
m = 0
t = ""
for i in s:
    if i == "D":
        t += i
        m = max(m,len(t))
        t = ""
    elif i == "C":
        t = ""
        t += i
    elif t and t[0] == "C":
        t += i

print(m)
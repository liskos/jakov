s = open("files/2__1iafi.txt").read()

t = ""
m = 0

for i in s:
    if t and (t[-1] != "E" or i != "F"):
        t += i
        m = max(m,len(t))
    else:
        t = i

print(m)
s = open("24data/24-2.txt").read()

t = ""
m = 0

for i in s:
    if t and i > t[-1]:
        t += i
        m = max(m,len(t))
    else:
        t = i

print(m)
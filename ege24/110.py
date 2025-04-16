s = open("24data/24-2.txt").read()

t = ""
m = 0

for i in s:
    if t and t[-1] > i:
        t += i
        m = max(m,len(t))
    else:
        t = i


print(m)
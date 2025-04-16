s = open("24data/24-1.txt").read()

m = 0
t = ""

for i in s:
    if t and t[-1] < i:
        t += i
        m = max(m,len(t))
    else:
        t = i


print(m)
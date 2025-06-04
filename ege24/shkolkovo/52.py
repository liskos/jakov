s = open("files/7__19jz8.txt").read()

t = ""
m = 0

for i in s:
    if len(t) > 1 and t[-1] != i and t[-2] != i:
        t += i
        m = max(m,len(t))
    elif t and t[-1] != i:
        t += i
        m = max(m,len(t))
    else:
        t = i
print(m)
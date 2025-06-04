s = open("files/7__19jz8.txt").read()

t = ""
m = 0

for i in s:
    if len(t) >= 2 and len(set([t[-2], t[-1], i])) == 3:
        t += i
        m = max(m, len(t))
    else:
        t = t[-1] + i if t and t[-1] != i else i
print(m)

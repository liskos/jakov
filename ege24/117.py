s = open("24data/24-4.txt").read()

t = ""
b = []
for i in s:
    if t and t[-1] > i:
        t += i
    else:
        b.append(t)
        t = i
b.append(t)
print(max(b,key=lambda x:len(x)))
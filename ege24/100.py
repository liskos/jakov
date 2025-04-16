s = open("24data/24-2.txt").read()

t = ""
b = []
for i in s:
    if t and t[-1] < i:
        t += i
    else:
        b.append([t,len(t)])
        t = i


print(max(b,key=lambda x:x[-1]))
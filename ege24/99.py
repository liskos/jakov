s = open("24data/24-1.txt").read()

t = ""
m = 0
b = []
for i in s:
    if t and t[-1] < i:
        t += i

    else:
        b.append([t,len(t)])
        t = i

print(b)
print(max(b, key = lambda x:x[-1])[0])


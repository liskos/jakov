s = open("24data/24-3.txt").read()

m = 0
t = ""
b = []
for i in s:
    if t and t[-1] > i:
        t += i
    else:
        b.append(t)
        t = i


print(max(b,key=lambda x:len(x)))
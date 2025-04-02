s = open("24data/k7b-1.txt").read()


t = "EAB"
while t in s:
    t += "EAB"
t = t[:-2]
print(t)
print(len(t))
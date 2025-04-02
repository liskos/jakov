s = open("24data/k7b-5.txt").read()

t = "CA"
while t in s:
    t += "CA"
while t not in s:
    t = t[:-1]

print(len(t))
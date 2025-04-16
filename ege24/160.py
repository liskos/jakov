s = open("24data/24-s1.txt").read()
print(s.count("J"))
k = 0
m = 1000
b = 0
d = ""
for line in s:
    if line.count("A") == 34:
        m = line
        break
for i in m:
    if m.count(i) > b:
        b = m.count(i)
        d = i
print(b,d)

#J
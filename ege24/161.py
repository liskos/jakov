s = open("24data/24-s1.txt").readlines()
k = 0
m = 0
b = 1000
d = ""
for line in s:
    if line.count("Q") == 64:
        m = line

for i in m:
    if m.count(i) < b:
        if i < m or str(b).isdigit():
            b = m.count(i)
            d = i
print(b,d)

#J
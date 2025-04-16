s = open("24data/24-s1.txt").readlines()
d = "V"
k = 100
m = 0
for line in s:
    for i in range(len(line)-1):
        if int(line[i],36) - int(line[i+1],36) == 1:
            m = line
            break

for i in m:
    if m.count(i) <= k and i < d:
        d = i
        k = m.count(i)
print(d)
print(k)
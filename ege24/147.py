s = open("24data/24-s2.txt").read()

b = []
t = ""
s = s.replace("0", "2").replace("\n", "")  # Удаляем \n из строки
for i in range(len(s)):
    if t and int(t[-1]) + int(s[i]) > 9:
        t += s[i]
    else:
        b.append(t)
        t = s[i]


print(len(max([x for x in b])))
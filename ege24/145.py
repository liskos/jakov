s = open("24data/24-j7.txt").read()

b = []
t = ""
s = s.replace("0", "2").replace("\n", "")  # Удаляем \n из строки
for i in range(len(s)):
    if t and int(t[-1]) % int(s[i]) == 0:
        t += s[i]
    else:
        b.append(t)
        t = s[i]


print(max([x for x in b]))
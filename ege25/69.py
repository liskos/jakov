p = 0
b = []
c = []
for n in range(64444,77563+1):
    s = str(n)
    if int(s[0]) % 2 == 0 and int(s[1]) % 2 == 0 and int(s[2]) % 2 != 0 and int(s[3]) % 2 != 0 and int(s[4]) % 2 != 0:
        b.append(n)
for n in b:
    if n % 9 != 0 and n % 13 != 0 and n % 17 != 0:
        c.append(n)

print(len(c),max(c)-min(c))


#238 4488
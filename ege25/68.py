# def proverk(n):
#     p = 0
#     n = int(str(n)[2:])
#     while n > 0:
#         if n % 2 == 0:
#             p += 1
#             n %= 10
#         else:
#             return False
#     if p == 3:
#         return True

p = 0
b = []
c = []
for n in range(57888,74555+1):
    s = str(n)
    if int(s[0]) % 2 != 0 and int(s[1]) % 2 != 0 and int(s[2]) % 2 == 0 and int(s[3]) % 2 == 0 and int(s[4]) % 2 == 0:
        b.append(n)
for n in b:
    if n % 6 != 0 and n % 7 != 0 and n % 8 != 0:
        c.append(n)

print(len(c),max(c)-min(c))

#146 14884
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
    a = [str(int(i) % 2) for i in str(n)]
    a = "".join(a)
    if a == "11000":
        b.append(n)
for n in b:
    if n % 9 != 0 and n % 7 != 0 and n % 13 != 0:
        c.append(n)

print(len(c),max(c)-min(c))

#146 14884
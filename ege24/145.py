s = open("24data/24-j7.txt").read()
#
# b = []
# t = ""
# s = s.replace("0", "2").replace("\n", "")  # Удаляем \n из строки
# for i in range(len(s)):
#     if t and int(t[-1]) % 2 == int(s[i]) % 2:
#         t += s[i]
#     else:
#         b.append(t)
#         t = s[i]
# b.append(t)
#
# print(max([len(x) for x in b]))
import re

pattern = r"([13579]+)|([02468]+)"
b = [len(x.group()) for x in re.finditer(pattern,s)]
print(max(b))
s = open("24data/24-1.txt").read()

# b = []
# k = ""
# for i in range(len(s)):
#     if s[i].isdigit():
#        k += s[i]
#     elif k and k[-1] in "02468":
#         b.append(int(k))
#         k = ""
#     else:
#         k = ""
# print(max(b))

import re

number = r"([1-9][0-9]*[02468]|[02468])"
pattern = rf"[^0-9]{number}[^0-9]"
r = [x.group() for x in re.finditer(pattern,s)]
print(r)
print(max([int(i[1:-1]) for i in r]))

# print(max(int(x) for x in s if x.isdigit() and int(x) % 2 == 0))
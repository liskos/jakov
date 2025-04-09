import string
s = open("24_21421.txt").read()

# for i in "CDEFGHIJKLMNOPQRSTUVWXYZ":
#     s = s.replace(i," ")
# while " 0" in s:
#     s = s.replace(" 0"," ")
# r = [i for i in s.split() if i[-1] in "02468A" ]
# m = max(r,key=len)
# print(m,len(m))

import re
number = r"([1-9AB][0-9AB]*[02468A]|[02468A])"
r = [i.group() for i in re.finditer(number, s)]
m = max(r, key=len)
print(len(m), m)
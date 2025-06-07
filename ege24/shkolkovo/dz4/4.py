s = open("files/24_3__6ao05.txt").read()

import re
num = r"([1-2][0-2]*|0)"
patt = rf"AB{num}([+*]{num})+"
b = max([x.group() for x in re.finditer(patt,s)],key=len)
print(len(b))
print(b)
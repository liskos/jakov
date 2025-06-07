s = open("files/24_1__6ba3v.txt").read()

import re

num = r"([1-6][0-6]*|0)"
patt = rf"{num}([+*]{num})+"

b = max([x.group() for x in re.finditer(patt,s)],key=len)

print(len(b))
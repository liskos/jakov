s = open("files/24_2__6anzj (1).txt").read()

import re

num = r"([1-7][0-7]*|0)"
patt = rf"{num}([+*]{num})+"

b = max([x.group() for x in re.finditer(patt,s)],key=len)
print(len(b))
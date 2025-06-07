s = open("24-2__63h4e (1).txt").read()

import re

num = r"([1-4][0-4]*|0)"

patt = rf"A{num}([+*]{num})+"

b = max([x.group() for x in re.finditer(patt,s)],key=len)

print(len(b))

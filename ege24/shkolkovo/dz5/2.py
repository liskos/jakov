s = open("files/24_1__6ba3v.txt").read()

import re

num = r"([1-9][0-9]*|0)"
patt = rf"{num}([+*]{num})+"

b = [x.group() for x in re.finditer(patt,s)]
b = max([x for x in b if eval(x) % 2 == 0],key=len)
print(eval(b))
print(len(b))
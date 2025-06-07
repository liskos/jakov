s = open("files/24_6__6ao27.txt").read()

import re

num = r"([1-9][0-9]*[0][0]+|0)"
patt = rf"{num}([-/]{num})+"

b = [x.group() for x in re.finditer(patt,s)]
b = max([x for x in b if x.count("-") + x.count("/") <= 10],key=len)
print(b)

print(len(b))
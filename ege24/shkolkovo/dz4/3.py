s = open("files/24_5__6ao1t.txt").read()

import re
num = r"([1-9][0-9]*|0)"
patt = rf"{num}([*]{num})+"

b = max([x.group() for x in re.finditer(patt,s)],key=eval)

print(eval(b))
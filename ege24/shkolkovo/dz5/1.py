s = open("files/24_2__6jwgo (1).txt").read()

import re

num = r"([1-9][0-9]*)"
patt = rf"{num}([-*]{num})+"

b = max([x.group() for x in re.finditer(patt,s)],key=len)
print(eval(b))
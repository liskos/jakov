s = open("24-1__63h3j (1).txt").read()

import re

num = r"([1-9][1-9]*|[1-9])"


patt = rf"[-]?{num}([+-]{num})+"

b = max([x.group() for x in re.finditer(patt,s)],key=len)

print(len(b))
s = open("files/24-2__63h4e.txt").read()

import re
num = r"([1-9][0-9]*|0)"
pat = rf"[A]{num}([+*]{num})+"

b = max([x.group() for x in re.finditer(pat,s)],key=len)
print(len(b))
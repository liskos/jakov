s = open("files/24-3__63h5x.txt").read()

import re
num = r"([1-9][0-9]*|0)"
pat = rf"{num}([+]{num})+"

b = max([x.group() for x in re.finditer(pat,s)],key=eval)
print(eval(b),b)
import re
import string
s = open("24_21908.txt").read()

num = r"[1-9abcd][0-9abcd]*[02468ac]"

b = [x.group() for x in re.finditer(num,s)]
b.sort(key=len)

print(len(b[-1]))
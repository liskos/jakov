import re
import string
s = open("24_21908.txt").read()
num = r"[1-9abcd][0-9abcd]*"
num = rf"{num}[02468ac]"

b = [(x.group()) for x in re.finditer(num,s)]
print(b)
print(len(max(b)))
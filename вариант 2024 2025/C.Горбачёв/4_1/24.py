s = open('24_18535.txt').read()

import re

num = r"(([1-9][0-9]*)|[0-9])"
operation = rf"{num}([+*]{num})+"
r = [len(x.group()) for x in re.finditer(operation,s)]

print(max(r))
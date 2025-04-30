s = open("24data/24-304.txt").read()

import re
numbers = r"([1-9][0-9]|0)"
numbers = rf"A{numbers}([*+]{numbers})+"

b = [len(x.group()) for x in re.finditer(numbers,s)]

print(max(b))
s = open("kege/24_21597.txt").read()

import re

num = r"([1-5][0-5]*|0)"
num = rf"{num}([-*]{num})+"
b = [len(x.group()) for x in re.finditer(num,s)]

print(max(b))
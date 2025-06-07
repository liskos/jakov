s = open("files/24_7__6ao2p.txt").read()

import re

num = r"[1-9][0-9]*"
num = rf"{num}([*]{num})+([+*]{num})*"

b = [(x.group()) for x in re.finditer(num,s)]
b = max(b,key=eval)
print(b)
print(eval(b))
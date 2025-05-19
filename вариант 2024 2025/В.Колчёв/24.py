s = open("24_18147.txt").read()
import re
num = r"[7-9]+"
prefetch = rf"(({num}[+])+{num})"

b = [x.group() for x in re.finditer(prefetch,s)]
m = max(b, key=eval)
print(eval(m), m)
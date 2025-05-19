s = open("24_18147.txt").read()
import re
num = r"[1-9][0-9]*|0"
prefetch = rf"(({num}[+])*{num}*)"

b = [(x.group()) for x in re.finditer(prefetch,s)]
b = sorted(b,key=lambda x:len(x))
print(b[-1])
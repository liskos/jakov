import re
s = open("24_22235(1).txt").read()
num = r"(([1-9][0-9]*[24568])|([024568]))"
proiz = rf"({num}[*])*0([*]{num})*"
summa = rf"({proiz}[+])*{proiz}"
b = [x.group() for x in re.finditer(summa,s)]
m = max(b, key=len)
print(len(m), m)
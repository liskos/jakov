import re
# s = open("24data/k7a-1.txt").readline()
#
# number = r"[ABC]+"
#
# b = ([len(x.group()) for x in re.finditer(number,s)])
#
# print(max(b))

# s = open("24data/24-196.txt").readline()
#
# numbers = r"(ZX|ZY)+"
# d = [len(x.group())//2 for x in re.finditer(numbers,s)]
#
# print(max(d))

# s = open("24data/24-310.txt").readline()

# number = r"(?=((AA|CC)+))"
# d = [len(x.group(1))//2 for x in re.finditer(number,s)]
# print(max(d)b )

# number = r"([123][ABC][123])+"
#
# number = rf"(?=({number}))"
#
# print(max(len(x.group(1))//3 for x in re.finditer(number,s)))

# number = r"(YZZ|XY|YZ)+"
# number = rf"(?=({number}))"
# print(max(len(x.group(1))//3 for x in re.finditer(number,s)))

# number = r"([1-9][0-9]*)"
# number = rf"{number}([-*]{number})+"
# b = [len(x.group()) for x in re.finditer(number,s)]
# print(max(b))
#
# number = r"[12][012]*|0"
# number = rf"{number}([+*]{number})*"
# b = [len(x.group()) for x in re.finditer(number,s)]
# print(max(b))

s = open("24data/24-299.txt").readline()

numbers = r"([1-9][0-9]*|0)"

proiz = rf"(({numbers}\*)*0(\*{numbers})*)"
reg = rf"{proiz} (\+{proiz})+".replace(" ","")
m = [len(x.group()) for x in re.finditer(reg,s)]
print(max(m))
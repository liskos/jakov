s = open("24data/24-296.txt").read()
#
l = 0
m = 10000
k = 0

ind = [x for x in range(len(s)-1) if s[x:x+2] == "AF"]
for i in range(len(ind)-200):
    m = min(ind[i+200] - ind[i] + 2,m)
print(m)

# import re
# numbers = r"(AF.*){200}AF"
# x = [len(x.group()) for x in re.finditer(numbers,s)]
#
# print(min(x))
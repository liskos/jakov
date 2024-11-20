def f(x):
    a = []
    if (x + 1) % 2 != 0:
        a.append(x+1)
    if (x+3) % 2 != 0:
        a.append(x+3)
    if x * 3 % 2 != 0:
        a.append(x*3)
    return a
a = [" "]* 160
for x in range(160):
    if x>= 51:
        a[x] = "0"

for x in range(51):
    if a[x] == " " and any(a[i] == "0" for i in f(x)):
        a[x] = "1"
for x in range(51):
    if a[x] == " " and all(a[i] == "1" for i in f(x)):
        a[x] = "2"
for x in range(51):
    if a[x] == " " and any(a[i] in "20" for i in f(x)):
        a[x] = "3"
for x in range(51):
    if a[x] == " " and all(a[i] in "13" for i in f(x)):
        a[x] = "4"
import sys
sys.stdout = open("38.xls",mode="x")
print(*a[1:60],sep="\t")


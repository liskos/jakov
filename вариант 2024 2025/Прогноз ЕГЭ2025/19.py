def f(x):
    if x % 2 == 0:
        return x - 3,x // 2
    return x - 3,(x + 3) // 2


a = [" "] * 500
for x in range(500):
    if x <= 24:
        a[x] = "0"

for x in range(400):
    if a[x] == " " and any(a[i] == "0" for i in f(x)):
        a[x] = "1"
for x in range(400):
    if a[x] == " " and all(a[i] == "1" for i in f(x)):
        a[x] = "2"
for x in range(400):
    if a[x] == " " and any(a[i] in "02" for i in f(x)):
        a[x] = "3"
for x in range(400):
    if a[x] == " " and all(a[i] in "13" for i in f(x)):
        a[x] = "4"

import sys
sys.stdout = open("19.xls",mode="x")
print(*a[1:400],sep="\t")
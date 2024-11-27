def f(x):
    return x+3,x*5

a = [" "] * 2000

for x in range(2000):
    if x >= 301:
        a[x] = "0"

for x in range(301):
    if a[x] == " " and any(a[i] == "0" for i in f(x)):
        a[x] = "1"

for x in range(301):
    if a[x] == " " and all(a[i] == "1" for i in f(x)):
        a[x] = "2"
for x in range(301):
    if a[x] == " " and any(a[i] in "02" for i in f(x)):
        a[x] = "3"
for x in range(301):
    if a[x] == " " and all(a[i] in "13" for i in f(x)):
        a[x] = "4"

import sys
sys.stdout = open("19.xls",mode="x")
print(*a[1:2000],sep="\t")
def f(x):
    return x+2,x*2

a = [" "]* 60
for x in range(60):
    if x>= 25:
        a[x] = "0"

for x in range(60):
    if a[x] == " " and any(a[i] == "0" for i in f(x)):
        a[x] = "1"
for x in range(60):
    if a[x] == " " and all(a[i] == "1" for i in f(x)):
        a[x] = "2"
for x in range(60):
    if a[x] == " " and any(a[i] in "20" for i in f(x)):
        a[x] = "3"
for x in range(60):
    if a[x] == " " and all(a[i] in "13" for i in f(x)):
        a[x] = "4"
import sys
sys.stdout = open("39.xls",mode="x")
print(*a[1:60],sep="\t")


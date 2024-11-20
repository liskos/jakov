def f(x):
    return x+3,x*2

a = [" "]* 80
for x in range(80):
    if x>= 33:
        a[x] = "0"

for x in range(80):
    if a[x] == " " and any(a[i] == "0" for i in f(x)):
        a[x] = "1"
for x in range(80):
    if a[x] == " " and all(a[i] == "1" for i in f(x)):
        a[x] = "2"
for x in range(80):
    if a[x] == " " and any(a[i] in "20" for i in f(x)):
        a[x] = "3"
for x in range(80):
    if a[x] == " " and all(a[i] in "13" for i in f(x)):
        a[x] = "4"
import sys
sys.stdout = open("40.xls",mode="x")
print(*a[1:80],sep="\t")


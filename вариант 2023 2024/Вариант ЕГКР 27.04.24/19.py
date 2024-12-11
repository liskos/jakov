def f(x):
    return x+5,x*3

a = [" "]* 1500
for x in range(1500):
    if x>= 435:
        a[x] = "0"

for x in range(1500):
    if a[x] == " " and any(a[i] == "0" for i in f(x)):
        a[x] = "1"
for x in range(1500):
    if a[x] == " " and all(a[i] == "1" for i in f(x)):
        a[x] = "2"
for x in range(1500):
    if a[x] == " " and any(a[i] in "20" for i in f(x)):
        a[x] = "3"
for x in range(1500):
    if a[x] == " " and all(a[i] in "13" for i in f(x)):
        a[x] = "4"
import sys
sys.stdout = open("19.xls",mode="x")
print(*a[1:1500],sep="\t")


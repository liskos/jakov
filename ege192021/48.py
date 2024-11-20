def f(x):
    return x+1,x*2,x*3

a = [" "]* 200
for x in range(200):
    if 72 >= x>= 43:
        a[x] = "0"
    if x > 72:
        a[x] = "8"
for x in range(43):
    if a[x] == " " and any(a[i] == "0" for i in f(x)):
        a[x] = "1"
for x in range(43):
    if a[x] == " " and all(a[i] in "18" for i in f(x)):
        a[x] = "2"
for x in range(43):
    if a[x] == " " and any(a[i] in "20" for i in f(x)):
        a[x] = "3"
for x in range(43):
    if a[x] == " " and all(a[i] in "138" for i in f(x)):
        a[x] = "4"
import sys
sys.stdout = open("48.xls",mode="x")
print(*a[1:200],sep="\t")


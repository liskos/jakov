def f(x):
    return x+1,x*2,x*3

a = [" "]* 200
for x in range(200):
    if x>= 43:
        a[x] = "0"

for x in range(200):
    if a[x] == " " and any(a[i] == "0" for i in f(x)):
        a[x] = "1"
for x in range(200):
    if a[x] == " " and all(a[i] == "1" for i in f(x)):
        a[x] = "2"
for x in range(200):
    if a[x] == " " and any(a[i] in "20" for i in f(x)):
        a[x] = "3"
for x in range(200):
    if a[x] == " " and all(a[i] in "13" for i in f(x)):
        a[x] = "4"
import sys
sys.stdout = open("48.xls",mode="x")
print(*a[1:200],sep="\t")


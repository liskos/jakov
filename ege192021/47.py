def f(x):
    return x+1,x*2,x*3

a = [" "]* 200
for x in range(200):
    if 60 >= x>= 36:
        a[x] = "0"
    if x > 60:
        a[x] = "9"
for x in range(200):
    if a[x] == " " and any(a[i] == "0" for i in f(x)):
        a[x] = "1"
for x in range(200):
    if a[x] == " " and all(a[i] in "19" for i in f(x)):
        a[x] = "2"

for x in range(200):
    if a[x] == " " and any(a[i] in "20" for i in f(x)):
        a[x] = "3"
for x in range(200):
    if a[x] == " " and all(a[i] in "139" for i in f(x)):
        a[x] = "4"
import sys
sys.stdout = open("47.xls",mode="x")
print(*a[1:200],sep="\t")


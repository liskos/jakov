def f(x):
    return (x+1),(x*2)

a = [" "]* 100
for x in range(100):
    if 30 <= x >= 20:
        a[x] = "0"
    if 20 <= x <= 30:
        a[x] = "8"
for x in range(100):
    if a[x] == " " and any(a[i] == "0" for i in f(x)):
        a[x] = "1"
for x in range(100):
    if a[x] == " " and all(a[i] in "18" for i in f(x)):
        a[x] = "2"
for x in range(100):
    if a[x] == " " and any(a[i] in "20" for i in f(x)):
        a[x] = "3"
for x in range(100):
    if a[x] == " " and all(a[i] in "138" for i in f(x)):
        a[x] = "4"
import sys
sys.stdout = open("80.xls",mode="x")
print(*a[1:100],sep="\t")


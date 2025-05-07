def f(x):
    return x+1,x+4,x*3

a = [" "] * 400

for x in range(400):
    if x >= 67:
        a[x] = "0"

for x in range(400):
    if a[x] == " " and any(a[j] == "0" for j in f(x)):
        a[x] = "1"
for x in range(400):
    if a[x] == " " and all(a[j] == "1" for j in f(x)):
        a[x] = "2"

for x in range(400):
    if a[x] == " " and any(a[j] in "02" for j in f(x)):
        a[x] = "3"

for x in range(400):
    if a[x] == " " and all(a[j] in "13" for j in f(x)):
        a[x] = "4"

print([i for i in range(1,400) if a[i] == "2"])
print([i for i in range(1,400) if a[i] == "3"])
print([i for i in range(1,400) if a[i] == "4"])
import sys
sys.stdout = open("19.xls",mode="x")

print(*a[1:400],sep="\t")

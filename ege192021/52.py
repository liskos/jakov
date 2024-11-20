import sys
def f(x):
    return x+100,x*2

a = [" "]*5000

for x in range(5000):
        if x >= 1000:
            a[x] = "0"

for x in range(1000):
    if a[x] == " " and any(a[i] == "0" for i in f(x)):
            a[x] = "1"
for x in range(1000):
    if a[x] == " " and all(a[i] == "1" for i in f(x)):
            a[x] = "2"
for x in range(1000):
    if a[x] == " " and any(a[i] in "02" for i in f(x)):
            a[x] = "3"
for x in range(1000):
    if a[x] == " " and all(a[i] in "13" for i in f(x)):
        a[x] = "4"

sys.stdout = open("52.xls",mode="x")
for i in range(1,5000):
    print(*a[i][1:5000],sep="\t")
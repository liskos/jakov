import sys
def f(x):
    if x % 2 == 0:
        return (x//2),(x - 5), (x - 4), (x - 3), (x - 2),(x - 1)
    return (x-5),(x-4),(x-3),(x-2),(x-1)

a = [" "]*200

for x in range(100):
        if x < 10:
            a[x] = "0"
for x in range(100):
        if a[x] == " " and any(a[i] == "0" for i in f(x)):
            a[x] = "1"
for x in range(100):
        if a[x] == " " and all(a[i] == "1" for i in f(x)):
            a[x] = "2"
for x in range(100):
        if a[x] == " " and any(a[i] in "02" for i in f(x)):
            a[x] = "3"
for x in range(100):
        if a[x] == " " and all(a[i] in "13" for i in f(x)):
            a[x] = "4"

sys.stdout = open("53.xls",mode="x")
for i in range(1,200):
    print(*a[i][1:200],sep="\t")
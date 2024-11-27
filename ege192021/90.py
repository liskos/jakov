def f(x,y):
    return (x+1,y),(x*3,y),(x,y+1),(x,y*3)

a = [[" "]*200 for _ in range(200)]

for x in range(200):
    for y in range(200):
        if x + y >= 60:
            a[x][y] = "0"
        if 79 <= x + y >= 60:
            a[x][y] = "8"

for x in range(60):
    for y in range(60):
        if a[x][y] == " " and any(a[i][j] == "0" for i,j in f(x,y)):
            a[x][y] = "1"
for x in range(60):
    for y in range(60):
        if a[x][y] == " " and all(a[i][j] in "18" for i,j in f(x,y)):
            a[x][y] = "2"
for x in range(60):
    for y in range(60):
        if a[x][y] == " " and any(a[i][j] in "20" for i,j in f(x,y)):
            a[x][y] = "3"
for x in range(60):
    for y in range(60):
        if a[x][y] == " " and all(a[i][j] in "183" for i,j in f(x,y)):
            a[x][y] = "4"
import sys
sys.stdout = open("90.xls",mode="x")
for i in range(1,200):
    print(*a[i][1:200],sep="\t")
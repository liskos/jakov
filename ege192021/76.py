def f(x,y):
    return (x+1,y),(x*3,y),(x,y*3),(x,y+1)

a = [[" "]* 300 for _ in range(300)]
for x in range(300):
    for y in range(300):
        if x+y>= 81:
            a[x][y] = "0"
for x in range(81):
    for y in range(81):
        if a[x][y] == " " and any(a[i][j] == "0" for i,j in f(x,y)):
            a[x][y] = "1"
for x in range(81):
    for y in range(81):
        if a[x][y] == " " and all(a[i][j] == "1" for i,j in f(x,y)):
            a[x][y] = "2"
for x in range(81):
    for y in range(81):
        if a[x][y] == " " and any(a[i][j] in "20" for i,j in f(x,y)):
            a[x][y] = "3"
for x in range(81):
    for y in range(81):
        if a[x][y] == " " and all(a[i][j] in "13" for i,j in f(x,y)):
            a[x][y] = "4"
import sys
sys.stdout = open("76.xls",mode="x")
for i in range(1,300):
    print(*a[i][1:300],sep="\t")


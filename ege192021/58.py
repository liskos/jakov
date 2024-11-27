def f(x,y):
    return (x+1,y),(x*4,y),(x,y+1),(x,y*4)

a = [[" "]* 550 for _ in range(550)]
for x in range(550):
    for y in range(550):
        if x+y>= 100:
            a[x][y] = "0"
for x in range(100):
    for y in range(100):
        if a[x][y] == " " and any(a[i][j] == "0" for i,j in f(x,y)):
            a[x][y] = "1"
for x in range(100):
    for y in range(100):
        if a[x][y] == " " and all(a[i][j] == "1" for i,j in f(x,y)):
            a[x][y] = "2"
for x in range(100):
    for y in range(100):
        if a[x][y] == " " and any(a[i][j] in "20" for i,j in f(x,y)):
            a[x][y] = "3"
for x in range(100):
    for y in range(100):
        if a[x][y] == " " and all(a[i][j] in "13" for i,j in f(x,y)):
            a[x][y] = "4"
import sys
sys.stdout = open("58.xls",mode="x")
for i in range(1,550):
    print(*a[i][1:550],sep="\t")


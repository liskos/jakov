def f(x,y):
    return (x+1,y),(x,y+1),(x*2,y),(x,y*2)

a = [[" "] * 150 for _ in range(150)]

for x in range(150):
    for y in range(150):
        if x+y >= 40:
            a[x][y] = "0"

for x in range(40):
    for y in range(40):
        if a[x][y] == " " and any(a[i][j] == "0" for i,j in f(x,y)):
            a[x][y] = "1"
for x in range(40):
    for y in range(40):
        if a[x][y] == " " and all(a[i][j] == "1" for i,j in f(x,y)):
            a[x][y] = "2"
for x in range(40):
    for y in range(40):
        if a[x][y] == " " and any(a[i][j] in "02" for i,j in f(x,y)):
            a[x][y] = "3"
for x in range(40):
    for y in range(40):
        if a[x][y] == " " and all(a[i][j] in "13" for i,j in f(x,y)):
            a[x][y] = "4"

import sys
sys.stdout = open("32.xls",mode="x")
for i in range(1,150):
    print(*a[i][1:150],sep = "\t")
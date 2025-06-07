def f(x,y):
    return (x + 1,y),(x,y+1),(x*3,y),(x,y*3)

a = [[" "] * 400 for _ in range(400)]

for x in range(400):
    for y in range(400):
        if x + y >= 65:
            a[x][y] = "0"

for x in range(400):
    for y in range(400):
        if a[x][y] == " " and any(a[i][j] == "0" for i,j in f(x,y)):
            a[x][y] = "1"

for x in range(400):
    for y in range(400):
        if a[x][y] == " " and all(a[i][j] == "1" for i,j in f(x,y)):
            a[x][y] = "2"

for x in range(400):
    for y in range(400):
        if a[x][y] == " " and any(a[i][j] in "02" for i,j in f(x,y)):
            a[x][y] = "3"

for x in range(400):
    for y in range(400):
        if a[x][y] == " " and all(a[i][j] in "13" for i,j in f(x,y)):
            a[x][y] = "4"

import sys
sys.stdout = open("19.xls",mode="x")

for i in range(400):
    print(*a[i][1:400],sep="\t")
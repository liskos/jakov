def f(x,y):
    return (x-2,y),(x//3,y),(x,y-2),(x,y//3)

a = [[" "] * 1500 for _ in range(1500)]

for x in range(200):
    for y in range(200):
        if x < 15 or y < 15:
            a[x][y] = "0"

for x in range(1500):
    for y in range(1500):
        if a[x][y] == " " and any(a[i][j] == "0" for i,j in f(x,y)):
            a[x][y] = "1"
for x in range(1500):
    for y in range(1500):
        if a[x][y] == " " and all(a[i][j] == "1" for i,j in f(x,y)):
            a[x][y] = "2"
for x in range(1500):
    for y in range(1500):
        if a[x][y] == " " and any(a[i][j] in "20" for i,j in f(x,y)):
            a[x][y] = "3"
for x in range(1500):
    for y in range(1500):
        if a[x][y] == " " and all(a[i][j] in "13" for i,j in f(x,y)):
            a[x][y] = "4"

import sys
sys.stdout = open("19.xls",mode="x")
for i in range(1,1500):
    print(*a[i][1:1500],sep = "\t")

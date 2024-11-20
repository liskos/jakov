import sys
def f(x,y):
    if (x / 2) % 2 != 0:
        return (x-1,y),(x,y-1),(x//2+1,y),(x,y//2)
    if (x / 2) % 2 != 0 and (y / 2) % 2 != 0:
        return (x - 1, y), (x, y - 1), (x // 2 + 1, y), (x, y // 2 + 1)
    if (y / 2) % 2 != 0:
        return (x-1,y),(x,y-1),(x//2,y),(x,y//2+1)
    return (x-1,y),(x,y-1),(x//2,y),(x,y//2)

a = [[" "]*200 for _ in range(200)]

for x in range(200):
    for y in range(200):
        if x+y <= 20:
            a[x][y] = "0"

for x in range(50):
    for y in range(50):
        if a[x][y] == " " and any(a[i][j] == "0" for i,j in f(x,y)):
            a[x][y] = "1"
for x in range(50):
    for y in range(50):
        if a[x][y] == " " and all(a[i][j] == "1" for i,j in f(x,y)):
            a[x][y] = "2"
for x in range(50):
    for y in range(50):
        if a[x][y] == " " and any(a[i][j] in "02" for i,j in f(x,y)):
            a[x][y] = "3"
for x in range(50):
    for y in range(50):
        if a[x][y] == " " and all(a[i][j] in "13" for i,j in f(x,y)):
            a[x][y] = "4"

sys.stdout = open("49.xls",mode="x")
for i in range(1,200):
    print(*a[i][1:200],sep="\t")
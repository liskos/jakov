def f(x,y):
    return (x-3,y),((x+1)//2,y),(x,y-3),(x,(y+1)//2)

a = [[" "]*400 for _ in range(400)]

for x in range(400):
    for y in range(400):
        if x + y <= 72:
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



print(max([s for s in range(23,400) if any(a[x][y] == "1" for x,y in f(s, 50))]))
print([s for s in range(23,400) if a[s][50] == "3"])
print([s for s in range(23,400) if a[s][50] == "4"])
a = [1]
for i in range(1,100):
    b = []
    for x in a:
        b.append(x+1)
        b.append(x+5)
        b.append(x*3)
    a = b.copy()
    if 111 in a:
        print(i)
        break
print(a.count(111))

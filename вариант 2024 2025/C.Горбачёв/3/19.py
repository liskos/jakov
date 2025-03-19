def f(x):
    return x-11,x//3

a = [" "] * 5000
for x in range(5000):
    if x <= 90:
        a[x] = "0"

for x in range(5000):
    if a[x] == " " and any(a[i] == "0" for i in f(x)):
        a[x] = "1"
for x in range(5000):
    if a[x] == " " and all(a[i] == "1" for i in f(x)):
        a[x] = "2"
for x in range(5000):
    if a[x] == " " and any(a[i] in "02" for i in f(x)):
        a[x] = "3"
for x in range(5000):
    if a[x] == " " and all(a[i] in "13" for i in f(x)):
        a[x] = "4"
for s in reversed(range(5000)):
    if any(a[x]=="1" for x in f(s)):
        print(s)
        break
print([x for x in range(5000) if s in f(x) ])
print([x for x in range(5000) if a[x]=="2"])
print([x for x in range(5000) if a[x]=="3"])
print([x for x in range(5000) if a[x]=="4"])
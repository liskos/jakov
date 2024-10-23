a = [int(x) for x in open("17data/17-1.txt")]

k = 0
d = 0
t = [a[0]]

for i in range(1,len(a)):
    if a[i] < t[-1]:
        t.append(a[i])
    else:
        t = [a[i]]
    if len(t) > d:
        d = len(t)
        k = 1
    elif len(t) == d:
        k += 1
print(d,k)
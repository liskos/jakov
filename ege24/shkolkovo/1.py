s = open("files/Задача_4__fz2o__tadu.txt").read()
k = 0
t = ""
m = 0
for i in s:
    if t and t[-1] != i:
        t += i
        m = max(m,len(t))
    else:
        t = i

print(m)
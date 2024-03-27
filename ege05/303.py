def f(n):
    s1,s2,s3,s4 = str(n)
    if int(s1) % 4 == 0:
        n = str(n)[1:]
        n = '9' + n
    elif int(s1) % 2 == 0 and int(s1) % 4 != 0:
        n = str(n)[1:]
        n = '3' + n
    return int(n)


n = 0
for i in range(1000,10000):
    if f(i) > 20:
        n += 1
print(n)
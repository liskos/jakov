def f(n):
    for i in (str(n)):
        if int(i) % 2 == 0:
            return False
    return True



k = 0

for n in range(1686,13276+1):
    if f(n):
        k += sum(map(int,str(n)))
print(k)

#13950
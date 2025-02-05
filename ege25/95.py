def f(n):
    massiv = [int(d) for d in str(n)]
    b = sorted(massiv)
    if massiv == b and len(massiv) == len(set(b)):
        return True
    else:
        return False


k = 0
for n in range(1395,22717+1):
    if f(n):
        k += n
print(k)


#1197473
def f(a):
    for x in range(1,1000000000):
        if not (not (not (x % 5490 == 0) and (x % a == 0) and (x % 6300 == 0)) or ((x % 5940 == 0) or (x % a != 0))):
            return False
    return True


for a in range(1,1000):
    if f(a):
        print(a)
        break
    else:
        print(a, "no ok")
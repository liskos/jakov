def f(x):
    return not(not(x % a == 0) and (x % 15 == 0)) or (not(x % 18 == 0) or not(x % 15 == 0))

for a in range(1,1000):
    if all([f(x) for x in range(1,1000)]):
        print(a)
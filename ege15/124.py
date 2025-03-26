def f(x):
    return (x % 18 != 0) or (x % 54 != 0) or (x % a == 0)

for a in range(1,1000):
    if all([f(x) for x in range(1,1000)]):
        print(a)
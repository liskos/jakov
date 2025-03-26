from itertools import product
for a in range(1, 1000):
    if all([(not(x <= 9) or (x * x <= a)) and (not(y * y <= a) or (y <= 10)) for x, y in product(range(1, 1000), repeat=2)]):
        print(a)

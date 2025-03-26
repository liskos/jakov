from itertools import product
for a in range(1,1000):
    if all([(x - 3 * y < a) or (y > 400) or (x > 56) for x,y in product(range(1,1000),repeat=2)]):
        print(a)
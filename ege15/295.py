from itertools import product
for a in range(1,1000):
    if all([(y+4*x < a)or (x + 4 * y > 120) or(5*x - 2 * y > 50) for x,y in product(range(1,1000),repeat=2)]):
        print(a)

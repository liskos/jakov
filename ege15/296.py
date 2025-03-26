from itertools import product
for a in range(1,1000):
    if all([(2*y+5*x < a)or (2*x + 4 * y > 100) or(3*x - 2 * y > 70) for x,y in product(range(1,1000),repeat=2)]):
        print(a)

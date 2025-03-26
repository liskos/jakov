from itertools import product
for a in range(1,1000):
    if all([(3*y+x < a)or (3*x + 2 * y > 80) or(3*x - 4 * y > 90) for x,y in product(range(1,1000),repeat=2)]):
        print(a)

from itertools import product
for a in range(1,1000):
    if all([(2*y-x < a)or (x + 2 * y > 50) or(2*x + y < 40) for x,y in product(range(1,1000),repeat=2)]):
        print(a)

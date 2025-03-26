from itertools import product
for a in range(1,1000):
    if all([(7*y+x < a)or (2*x + 3 * y > 98) for x,y in product(range(1,1000),repeat=2)]):
        print(a)

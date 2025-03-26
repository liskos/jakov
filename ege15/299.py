from itertools import product
for a in range(1,1000):
    if all([(y-x<a) or (7*x + 4*y > 350) or (3*y - 2 * x > 45) for x,y in product(range(1,1000),repeat=2)]):
        print(a)
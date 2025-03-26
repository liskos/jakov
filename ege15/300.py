from itertools import product
for a in range(1,1000):
    if all([(y-x>a) or (x+ 4*y > 40) or (y - 2*x < -35) for x,y in product(range(1,1000),repeat=2)]):
        print(a)
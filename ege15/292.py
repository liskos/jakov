from itertools import product
for a in range(1,1000):
    if all([(y+2*x < a)or (x > 20) or (y > 40) for x,y in product(range(1,1000),repeat=2)]):
        print(a)

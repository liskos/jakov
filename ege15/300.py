from itertools import product
import time
t1 = time.time()
for a in range(-100,1000):
    f = False
    for x in range(1, 1000):
        for y in range(1, 1000):
            t = (y-x>a) or (x+ 4*y > 40) or (y - 2*x < -35)
            if not t:
                f = True
                break
        if f:
            break
    else:
        print(a)
print(time.time()-t1)
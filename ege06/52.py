import math

s = 0
for x in range(0, int(300*math.cos(math.pi/6))+1):
    for y in range(-int(math.tan(math.pi/6)*x), int(math.tan(math.pi/6)*x)+1):
        s += 1
print(s)
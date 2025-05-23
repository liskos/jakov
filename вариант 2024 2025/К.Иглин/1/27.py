import math
import turtle
def clasterizasion(data):
    clasters = [[],[]]
    for x,y in data:
        if y > 4.5 and x > 0:
            clasters[0].append([x,y])
        else:
            clasters[1].append([x,y])

    return clasters


def visual(clasters):
    turtle.up()
    turtle.tracer(0)
    colors = ["red","yellow","purple","pink","blue","grey","orange"]
    for i,claster in enumerate(clasters):
        for x,y in claster:
            turtle.goto(x*8,y*8)
            turtle.dot(7,colors[i%len(colors)])
    turtle.done()

def get_centroid(claster):
    point = [0, 0]
    s = 10**10
    for p1 in claster:
        d = sum(math.dist(p1, p2) for p2 in claster)
        if d < s:
            s = d
            point = p1
    return point

def get_negotiv(claster):
    point = [0, 0]
    s = 0
    for p1 in claster:
        d = sum(math.dist(p1, p2) for p2 in claster)
        if d > s:
            s = d
            point = p1
    return point

def get_koef(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    k = (y2-y1) / (x2 - x1)
    b = y1 - k * x1
    return k, b

def peres(k1, k2, b1, b2):
    x = (b2-b1)/(k1-k2)
    y = k1 * x + b1
    return x,y

data = [list(map(float,line.split())) for line in open("27A_18565.txt")]
clasters = clasterizasion(data)
print(clasters)
centroid = [get_centroid(c) for c in clasters]
negativ = [get_negotiv(c) for c in clasters]
print(centroid)
print(negativ)
k1, b1 = get_koef(centroid[0], centroid[1])
k2, b2 = get_koef(negativ[0], negativ[1])
x, y = peres(k1,k2,b1,b2)
print(x * 100, y * 100)
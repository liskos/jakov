import math
import turtle


def clasterizasion(data,r):
    clasters = []
    while data:
        clasters.append([data.pop()])
        for p1 in clasters[-1]:
            sosedi = [p2 for p2 in data if math.dist(p1,p2)<=r]
            clasters[-1].extend(sosedi)
            for p in sosedi:
                data.remove(p)
    return clasters

def visual(clasters):
    turtle.up()
    turtle.tracer(0)
    colors = ["red","yellow","blue","orange","purple"]
    for i,claster in enumerate(clasters):
        for x,y in claster:
            turtle.goto(x*1,y*1)
            turtle.dot(7,colors[i%len(colors)])
    turtle.done()

def get_centroid(claster):
    r = []
    for p1 in claster:
        r += [[sum(math.dist(p1,p2) for p2 in claster),p1]]
    return min(r)[1]


data = [list(map(float,line.split())) for line in open("files/1_A__5wyzi (1).txt")]
data = [[x[0],x[1]] for x in data if 9 < x[2] < 13]
clasters = clasterizasion(data,4)
clasters = [c for c in clasters if len(c) > 20]
centroid = [get_centroid(c) for c in clasters]
x,y = sum(x[0] for x in centroid) / len(centroid),sum(x[1] for x in centroid) / len(centroid)
print(x*500,y*500)

data = [list(map(float,line.split())) for line in open("files/1_B__5wyzk.txt")]
data = [[x[0],x[1]] for x in data if 3 < x[2] < 8]
clasters = clasterizasion(data,4.5)
clasters = [c for c in clasters if len(c) > 20]
centroid = [get_centroid(c) for c in clasters]
x,y = sum(x[0] for x in centroid) / len(centroid),sum(x[1] for x in centroid) / len(centroid)
print(x*500,y*500)

import math,turtle
def clasterizasion(data,r):
    clasters = [[],[]]
    for x,y in data:
        if x < 23:
            clasters[0].append([x,y])
        else:
            clasters[1].append([x,y])
    return clasters

def clasterizasion2(data):
    clasters = [[],[],[]]
    for x,y in data:
        if x > 20:
            clasters[0].append([x,y])
        elif x > -10 and x < 20:
            clasters[1].append([x,y])
        else:
            clasters[2].append([x,y])
    return clasters
def visual(clasters):
    turtle.up()
    turtle.tracer(0)
    colors = ["red","blue","yellow","grey","orange"]
    for i,claster in enumerate(clasters):
        for x,y in claster:
            turtle.goto(x*5,y*5)
            turtle.dot(5,colors[i%len(colors)])
    turtle.done()


def get_centroid(claster):
    r = []
    for p1 in claster:
        r += [[sum(abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])for p2 in claster),p1]]
    return min(r)[1]

data = [list(map(float,line.split())) for line in open("27_A_18314.txt")]
clasters = clasterizasion(data,0.5)
centroid = [get_centroid(c) for c in clasters]
x,y = sum(x[0] for x in centroid)/len(centroid),sum(x[1] for x in centroid) / len(centroid)
print(x*1000,y*1000)

data = [list(map(float,line.split())) for line in open("27_B_18314.txt")]
clasters = clasterizasion2(data)
centroid = [get_centroid(c) for c in clasters]
visual(clasters)
x,y = sum(x[0] for x in centroid)/len(centroid),sum(x[1] for x in centroid) / len(centroid)
print(x*1000,y*1000)
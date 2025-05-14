import math,turtle
def clasterizasion(data,r):
    clasters = []
    while data:
        clasters.append([data.pop()])
        for p1 in clasters[-1]:
            sosedi = [p2 for p2 in data if math.dist(p1,p2) <= r]
            clasters[-1].extend(sosedi)
            for p in sosedi:
                data.remove(p)
    return clasters


def visual(clasters):
    turtle.up()
    turtle.tracer(0)
    colors = ["red","blue","orange","pink","purple"]
    for i,claster in enumerate(clasters):
        for x,y in claster:
            turtle.goto(x*8,y*8)
            turtle.dot(7,colors[i%len(colors)])
    turtle.done()

def get_centroid(claster):
    r = []
    for p1 in claster:
        r += [[sum(math.dist(p1,p2) for p2 in claster),p1]]

    return min(r)[1]

data = [list(map(float,line.split())) for line in open("27A_22238.txt")]
clasters = clasterizasion(data,1)
centroid = [get_centroid(c) for c in clasters]
x,y = sum(x[0] for x in centroid) / len(centroid),sum(x[1] for x in centroid) / len(centroid)
print(x*10000,y*10000)

data = [list(map(float,line.split())) for line in open("27B_22238.txt")]
clasters = clasterizasion(data,1)
visual(clasters)
centroid = [get_centroid(c) for c in clasters]
x,y = sum(x[0] for x in centroid) / len(centroid),sum(x[1] for x in centroid) / len(centroid)
print(x*10000,y*10000)
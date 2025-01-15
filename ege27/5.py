import math,turtle


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
    colors = ["pink","red","yellow","pink","blue","green"]
    for i,clasters in enumerate(clasters):
        for x,y in clasters:
            turtle.goto(x*50,y*50)
            turtle.dot(15,colors[i%len(colors)])
    turtle.done()


def get_centroid(claster):
    r = []
    for p1 in claster:
        r += [[sum(math.dist(p1,p2)for p2 in claster),p1]]
    return min(r)[1]

data = [list(map(float,line.split()))for line in open()]
clasters = clasterizasion(data,0.8)
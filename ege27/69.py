import turtle,math
def clasterizasion(data,r):
    clasters = []
    while data:
        clasters.append([data.pop()])
        for p1 in clasters[-1]:
            sosedi = [p2 for p2 in data if math.dist(p1,p2)<= r]
            clasters[-1].extend(sosedi)
            for p in sosedi:
                data.remove(p)
    return clasters


def visual(clasters):
    turtle.up()
    turtle.tracer(0)
    colors = ["red","yellow","green","blue","black","orange"]
    for i,claster in enumerate(clasters):
        for x,y in claster:
            turtle.goto(x*30,y*30)
            turtle.dot(5,colors[i%len(colors)])
    turtle.done()


def get_centroid(claster):
    r = []
    for p1 in claster:
        r += [[sum(math.dist(p1,p2) for p2 in claster),p1]]
    return min(r)[1]

data = [list(map(float,line.split())) for line in open("27data/27-69a.txt")]
clasters = clasterizasion(data,0.5)
centroid = [get_centroid(c) for c in clasters]
x, y = sum(x[0] for x in centroid) / len(centroid), sum(x[1] for x in centroid) / len(centroid)
print(x*10000,y*10000)

data = [list(map(float,line.split())) for line in open("27data/27-69b.txt")]
clasters = clasterizasion(data,0.5)
centroid = [get_centroid(c) for c in clasters]
x, y = sum(x[0] for x in centroid) / len(centroid), sum(x[1] for x in centroid) / len(centroid)
visual(clasters)
print(x*10000,y*10000)

#36305 54432
#41821 49335
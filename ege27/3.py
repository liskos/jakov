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
    colors = ["red","yellow","green"]
    for i,claster in enumerate(clasters):
        for x,y in claster:
            turtle.goto(x*50,y*50)
            turtle.dot(5,colors[i%len(colors)])
    turtle.done()


def get_centroid(claster):
    r = []
    for p1 in claster:
        r += [[sum(math.dist(p1,p2) for p2 in claster),p1]]
    return min(r)[1]
#-386666 454929
#-451641 146360


data = [list(map(float,line.split())) for line in open("27data/27-3a.txt")]
clasters = clasterizasion(data,0.8)
centroid = [get_centroid(c) for c in clasters]
x, y = sum(x[0] for x in centroid) / len(centroid), sum(x[1] for x in centroid) / len(centroid)
print(x*1000,y*1000)
visual(clasters)
data = [list(map(float,line.split())) for line in open("27data/27-3b.txt")]
clasters = clasterizasion(data,0.8)
# centroid = [get_centroid(c) for c in clasters]
# x,y = sum(x[0] for x in centroid) / len(centroid), sum(x[1] for x in centroid) /len(centroid)
# print(x*1000,y*1000)

#3205.588071839624 5809.796800593944

#3188.6396106794396 2583.419639070489

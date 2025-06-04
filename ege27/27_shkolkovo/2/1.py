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
    colors = ["red","pink","yellow","orange","black"]
    for i,claster in enumerate(clasters):
        for x,y in claster:
            turtle.goto(x*25,y*25)
            turtle.dot(15,colors[i%len(colors)])
    turtle.done()

def get_centroid(claster):
    r = []
    for p1 in claster:
        r += [[sum(math.dist(p1,p2)for p2 in claster),p1]]
    return min(r)[1]

data = [list(map(float,line.split())) for line in open("files/1A__4vjfn.txt")]
clasters = clasterizasion(data,0.7)
clasters = [c for c in clasters if len(c) > 20]
centroid = [get_centroid(c) for c in clasters]
x, y = sum(x[0] for x in centroid) / len(centroid), sum(x[1] for x in centroid) / len(centroid)
print(x*1000,y*1000)
data = [list(map(float,line.split())) for line in open("files/1B__4vjfp.txt")]
clasters = clasterizasion(data,0.6)
clasters = [c for c in clasters if len(c) > 20]
centroid = [get_centroid(c) for c in clasters]
x, y = sum(x[0] for x in centroid) / len(centroid), sum(x[1] for x in centroid) / len(centroid)
visual(clasters)
print(x*1000,y*1000)

#-5013 10862
#53853 38954
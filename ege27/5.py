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

data = [list(map(float,line.split()))for line in open("27data/27-5a.txt")]
clasters = clasterizasion(data,0.8)
centroid = [get_centroid(c)for c in clasters]
x, y = sum(x[0] for x in centroid) / len(centroid), sum(x[1] for x in centroid) / len(centroid)
print(x*10000,y*10000)
data = [list(map(float,line.split()))for line in open("27data/27-5b.txt")]
clasters = clasterizasion(data,0.8)
centroid = [get_centroid(c)for c in clasters]
x, y = sum(x[0] for x in centroid) / len(centroid), sum(x[1] for x in centroid) / len(centroid)
print(x*10000,y*10000)
visual(clasters)

#5994 -3453
#5135 53288
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
    colors = ["red","pink","black","yellow","orange"]
    for i,claster in enumerate(clasters):
        for x,y in claster:
            turtle.goto(x*15,y*15)
            turtle.dot(10,colors[i%len(colors)])
    turtle.done()

def get_centroid(claster):
    r = []
    for p1 in claster:
        r += [[sum(math.dist(p1,p2)for p2 in claster),p1]]
    return min(r)[1]

data = [list(map(float,line.split()))for line in open("27data/27-33a.txt")]
clasters = clasterizasion(data,0.7)
centroid = [get_centroid(c) for c in clasters]
x,y = sum(x[0] for x in centroid) / len(centroid), sum(x[1]for x in centroid) / len(centroid)
print(x*100000,y*100000)

data = [list(map(float,line.split()))for line in open("27data/27-33b.txt")]
clasters = clasterizasion(data,0.7)
centroid = [get_centroid(c) for c in clasters]
x,y = get_centroid(centroid)
visual(clasters)
print(x*10000,y*10000)

#30244 10311
#50808 78925
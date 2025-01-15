import turtle,math

def clasterization(data,r):
    clasters = []
    while data:
        clasters.append([data.pop()])
        for p1 in clasters[-1]:
            sosedi = [p2 for p2 in data if abs(p1[0]-p2[0])+abs(p1[1]-p2[1]) <= r]
            clasters[-1].extend(sosedi)
            for p in sosedi:
                data.remove(p)
    return clasters


def visual(clasters):
    turtle.up()
    turtle.tracer(0)
    colors = ["red","yellow","pink","blue"]
    for i,clasters in enumerate(clasters):
        for x,y in clasters:
            turtle.goto(x*4,y*4)
            turtle.dot(5,colors[i%len(colors)])
    turtle.done()

def get_centroid(claster):
    r = []
    for p1 in claster:
        r += [[sum(abs(p1[0]-p2[0])+abs(p1[1]-p2[1]) for p2 in claster),p1]]
    return min(r)[1]

data = [list(map(float,line.split()))for line in open("27_A_18314.txt")]
clasters = clasterization(data,3)

centroid = [get_centroid(c) for c in clasters]
x,y = sum(x[0] for x in centroid) / len(centroid), sum(x[1] for x in centroid) / len(centroid)
print(x*1000,y*1000)

data = [list(map(float,line.split()))for line in open("27_B_18314.txt")]
clasters = clasterization(data,3)
print([len(c) for c in clasters])
visual(clasters)

centroid = [get_centroid(c) for c in clasters]
x,y = sum(x[0] for x in centroid) / len(centroid), sum(x[1] for x in centroid) / len(centroid)
print(x*1000,y*1000)

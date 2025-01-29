import turtle,math

def clasterization(data,r):
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
    colors = ["red","blue","pink","black"]
    for i,clasters in enumerate(clasters):
        for x,y in clasters:
            turtle.goto(x*15,y*15)
            turtle.dot(5,colors[i%len(colors)])
    turtle.done()

def get_centroid(claster):
    r = []
    for p1 in claster:
        r += [[sum(math.dist(p1,p2)for p2 in claster),p1]]
    return min(r)[1]

data = [list(map(float,line.split()))for line in open("27data/27-31a.txt")]
clasters = clasterization(data,0.7778889)
clasters =  [c for c in clasters if len(c) > 8]
centroid = [get_centroid(c)for c in clasters]
print([len(c) for c in clasters])
x, y = sum(x[0] for x in centroid) / len(centroid),sum(x[1] for x in centroid) / len(centroid)

print(x*10000,y*10000)


data = [list(map(float,line.split()))for line in open("27data/27-31b.txt")]
clasters = clasterization(data,0.4)
print([len(c) for c in clasters])
clasters =  [c for c in clasters if len(c) > 8]
centroid = [get_centroid(c)for c in clasters]
x, y = sum(x[0] for x in centroid) / len(centroid),sum(x[1] for x in centroid) / len(centroid)
visual(clasters)

print(x*10000,y*10000)

#10456 -19959
# 10000 5041
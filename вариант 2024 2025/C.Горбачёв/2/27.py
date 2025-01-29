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
    colors = ["red","blue","yellow","grey","black","orange","purple"]
    for i,claster in enumerate(clasters):
        for x,y in claster:
            turtle.goto(x*15,y*15)
            turtle.dot(8,colors[i%len(colors)])
    turtle.done()

def get_centroid(claster):
    r = []
    for p1 in claster:
        r += [[sum(math.dist(p1,p2)for p2 in claster),p1]]
    return min(r)[1]

data = [list(map(float,line.split()))for line in open("27A_18539.txt")]
clasters = clasterizasion(data,1)
print([len(c)for c in clasters])

clasters = [c for c in clasters if len(c) > 30]
centroid = [get_centroid(c) for c in clasters]
s = math.dist(centroid[0],centroid[1])
print(s)
data = [list(map(float,line.split()))for line in open("27B_18539.txt")]
clasters = clasterizasion(data,0.5)


print([len(c)for c in clasters])
clasters = [c for c in clasters if len(c) > 30]
centroid = [get_centroid(c) for c in clasters]
s1 = math.dist(centroid[0],centroid[1])
s2 = math.dist(centroid[0],centroid[2])
s3 = math.dist(centroid[1],centroid[2])
print(s1 + s2 + s3)

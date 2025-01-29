import turtle,math,tkinter
def clasterizasion(data,r):
    clasters = [[],[],[]]
    for x,y in data:
        if x < 5:
            clasters[0].append([x,y])
        elif y < 5:
            clasters[1].append([x,y])
        else:
            clasters[2].append([x,y])

    return clasters
def clasterizasion2(data,r):
    clasters = [[],[],[],[],[]]
    for x,y in data:
        if x < 10 and y < x:
            clasters[0].append([x,y])
        elif x < 10 and y > x:
            clasters[1].append([x,y])
        elif y < 10 and x > 10:
            clasters[2].append([x,y])
        elif y < x:
            clasters[3].append([x,y])
        elif y > x:
            clasters[4].append([x,y])
        else:
            print("error")
    return clasters
def visual(clasters):
    turtle.up()
    turtle.tracer(0)
    colors = ["red","pink","cyan","blue","yellow","orange","purple"]
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


data = [list(map(float,line.split()))for line in open("27data/27-63a.txt")]
clasters = clasterizasion(data,0.5)
centroid = [get_centroid(c)for c in clasters]
x,y = sum(x[0] for x in centroid) / len(centroid),sum(x[1] for x in centroid) / len(centroid)
print(x*100000,y*100000)

data = [list(map(float,line.split()))for line in open("27data/27-63b.txt")]
clasters = clasterizasion2(data,3)
visual(clasters)
centroid = [get_centroid(c)for c in clasters]

x,y = sum(x[0] for x in centroid) / len(centroid),sum(x[1] for x in centroid) / len(centroid)
print(x*100000,y*100000)
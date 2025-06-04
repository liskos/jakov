import turtle,math
def clasterizasion(data, r):
    clasters = []
    while data:
        clasters.append([data.pop()])
        for p1 in clasters[-1]:
            sosedi = [p2 for p2 in data if ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5 <= r]
            clasters[-1].extend(sosedi)
            for p in sosedi:
                data.remove(p)
    return clasters

def visual(clasters):
    turtle.up()
    turtle.tracer(0)
    colors = ["red","green","yellow","blue","black","orange"]
    for i,claster in enumerate(clasters):
        for x, y in claster:
            turtle.goto(x*15, y*15)
            turtle.dot(7,colors[i%len(colors)])
    turtle.done()
def get_centroid(claster):
    r = []
    for p1 in claster:
        r += [[sum(((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5 for p2 in claster), p1]]
    return min(r)[1]



data = [list(map(float,line.split())) for line in open("files/27_A_3__4uxh4.txt")]
clasters = clasterizasion(data, 2)
centroid = [get_centroid(c) for c in clasters]
x, y = sum(x[0] for x in centroid) / len(centroid),  sum(x[1] for x in centroid) / len(centroid)
print((x*100), (y*100))

data = [list(map(float,line.split())) for line in open("files/27_B_3__4uxh6.txt")]
clasters = clasterizasion(data, 1)
visual(clasters)
centroid = [get_centroid(c) for c in clasters]
x, y = sum(x[0] for x in centroid) / len(centroid),  sum(x[1] for x in centroid) / len(centroid)
print(x*100, y*100)
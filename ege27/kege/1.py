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
    colors = ["red","blue","pink","yellow","green","orange"]
    for i,claster in enumerate(clasters):
        for x,y in claster:
            turtle.goto(x*20,y*20)
            turtle.dot(7,colors[i%len(colors)])
    turtle.done()

def get_controid(claster):
    r = []
    for p1 in claster:
        r += [[sum(math.dist(p1,p2)for p2 in claster),p1]]
    return min(r)[1]


data = [list(map(float,line.split()))for line in open("27_A_21932.txt")]
clasters = clasterizasion(data,2.33)
visual(clasters)
clasters1 = [c for c in clasters if min(clasters) == c]
clasters2 = [c for c in clasters if max(clasters) == c]

centroid1 = [get_controid(c) for c in clasters1]
centroid2 = [get_controid(c) for c in clasters2]

x,y = sum(x[0] for x in centroid1),sum(x[1] for x in centroid2)
print(abs(x*10000),y*10000)

data = [list(map(float,line.split()))for line in open("27_B_21932.txt")]
clasters = clasterizasion(data,1)

clasters = [c for c in clasters if min(clasters) == c]
centroid = [get_controid(c) for c in clasters]
x,y = sum(x[0] for x in centroid) / len(centroid),sum(x[1] for x in centroid) / len(centroid)
print(abs(x*10000),abs(y*10000))

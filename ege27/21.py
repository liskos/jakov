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
    colors = ["red","pink","yellow","black","orange","green","purple"]
    for i,claster in enumerate(clasters):
        for x,y in claster:
            turtle.goto(x*30,y*30)
            turtle.dot(10,colors[i%len(colors)])
    turtle.done()

def get_max_min(claster1,claster2):
    r = []
    for p1 in claster1:
        r+= [math.dist(p1,p2)for p2 in claster2]
    return max(r),min(r)


data = [list(map(float,line.split())) for line in open("27data/27-21a.txt")]
clasters = clasterizasion(data,1)
clasters.remove(clasters[2])
print([len(c)for c in clasters])

d_max,d_min = get_max_min(clasters[0],clasters[1])
print(d_min*10000,d_max*10000)

data = [list(map(float,line.split())) for line in open("27data/27-21b.txt")]
clasters = clasterizasion(data,1)
print([len(c)for c in clasters])

clasters.remove(clasters[2])

d_max,d_min = get_max_min(clasters[0],clasters[1])
print(d_min*10000,d_max*10000)

#52076 47744
#57501 43022
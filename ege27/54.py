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
    colors = ["red","yellow","green"]
    for i,claster in enumerate(clasters):
        for x,y in claster:
            turtle.goto(x*50,y*50)
            turtle.dot(5,colors[i%len(colors)])
    turtle.done()


import math
import turtle
def clasterizasion(data):
    clasters = []
    for x,y in data:
        if y > 4.5 and x > 0:
            clasters.append([x,y])
        else:
            clasters.append([x,y])

    return clasters


def visual(clasters):
    turtle.up()
    turtle.tracer(0)
    colors = ["red","yellow","purple","pink","blue","grey","orange"]
    for i,claster in enumerate(clasters):
        for x,y in claster:
            turtle.goto(x*8,y*8)
            turtle.dot(7,colors[i%len(colors)])
    turtle.done()

def get_centroid(claster):
    r = []
    for p1 in claster:
        r += [[]]
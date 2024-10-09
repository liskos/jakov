def f(cl_a,cl_b):
    xa,ya,xb,yb = 0,0,0,0
    s = 10**5
    for x1,y1 in cl_a:
        for x2,y2 in cl_b:
            r = ((x2-x1)**2+(y2-y1)**2)**0.5
            if r < s:
                s = r
                xa = x1
                ya = y1
                xb = x2
                yb = y2
    return s,(xa+xb)*1000,(ya+yb)*1000
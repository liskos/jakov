def s(p,star):
    r = 0
    k = 0
    for x,y in star:
        d = ((x-p[0])**2 + (y - p[1])**2) ** 0.5
        if p[2] <= d <= p[2]*3:
            r += d
            k += 1
    return r / k * 1000
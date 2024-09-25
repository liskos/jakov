def func(kl):
    xc = 0
    yc = 0
    s = 10**10
    for a in kl:
        r = 0
        for b in kl:
            r += ((a[0]-b[0])**2 + (a[1] - b[1]) ** 2)**0.5
        if r < s:
            s = r
            xc = a[0]
            yc = a[1]
    return xc,yc
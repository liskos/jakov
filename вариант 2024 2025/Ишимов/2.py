for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = not(z or (not w or y))or(not x or z)
                if not f:
                    print(x,y,z,w,"!",int(f))
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = (not w or not(z==y)) and(z or (not y or x))
                if not f:
                    print(x,y,z,w,"!",int(f))
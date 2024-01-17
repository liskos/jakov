for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = not w and(x and not z or not x and not y and z)
                if f:
                    print(x,y,z,w,"!",int(f))
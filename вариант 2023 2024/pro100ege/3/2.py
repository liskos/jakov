for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = not(not x or not(not z or w))and(z or ( w != y))
                print(x,y,z,w,"!",int(f))
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f=not(not w or z)or(not x or y)or not x
                if not f:
                    print(x,y,z,w,"!",int(f))

for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f=not x or((not w or y)!=z)
                print(x,y,z,w,"!",int(f))
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f=((not x or y)or not(not z or w))and((not w or not x)or(y or z))
                if not f:
                    print(x,y,z,w,"!",int(f))
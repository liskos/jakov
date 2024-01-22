for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f=(not((not z or y)and(x or w)))or((z==w)or(y and not x))
                if not f:
                    print(x,y,z,w,"!",int(f))
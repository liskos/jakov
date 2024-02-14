for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f1=(not x or y)or(not w==z)
                f2=(not x or y)==(x and not z)
                print(x,y,z,w,"!",int(f1),int(f2))
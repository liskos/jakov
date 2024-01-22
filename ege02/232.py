for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f=w and((not x or y)==(not y or z))
                if f:
                     print(x,y,z,w,"!",int(f))
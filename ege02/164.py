for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f =not y or x or(not z and w)
                if not f:
                    print(w,x,z,y,"!",int(f))
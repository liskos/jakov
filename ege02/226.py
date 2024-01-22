for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            f=not(z or x)or y and not x and (z and not y or z)
            if f:
                 print(x,y,z,"!",int(f))
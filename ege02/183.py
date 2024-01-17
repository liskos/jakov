for x in 0,1:
    for y in 0,1:
        for z in 0,1:
<<<<<<< HEAD
            f=(not y or x)and z and not(z==y)
=======
            f = (not y or x)and z and not (z==y)
>>>>>>> origin/master
            if f:
                print(x,y,z,"!",int(f))
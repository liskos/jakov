for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = (x and not y) or (x == z) or w
                if not f:
                    print(x,y,z,w,"!",int(f))

z yx w
1000
1100
0110
for a in 0,1:
    for b in 0,1:
        for c in 0,1:
            for d in 0,1:
                f = ((not a or b) == c) or d
                if not f:
                    print(a,b,c,d,"!",int(f))
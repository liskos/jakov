for a in 0,1:
    for b in 0,1:
        for c in 0,1:
            for d in 0,1:
                f=(a or b)and(b==(not c))and not d
                if f:
                    print(a,b,c,d,"!",int(f))
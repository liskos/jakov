for a in 0,1:
    for b in 0,1:
        for c in 0,1:
            for d in 0,1:
                f= (a and not b) or ((a or b)and c) or d
                if not f:
                    print(a,b,c,d,"!",int(f))
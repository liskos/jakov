for a in 0,1:
    for b in 0,1:
        for c in 0,1:
            for d in 0,1:
                f=(not a or b)and not(b==c)and(not d or a)
                if f:
                    print(a,b,c,d,"!",int(f))

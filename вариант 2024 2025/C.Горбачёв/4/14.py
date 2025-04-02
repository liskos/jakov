for p in range(37):
    for s in range(35):
        try:
            f = int("R4",p-1) + int("B0",s+2) + int("T3NK4",p)
            if f == 23593399:
                print(p*s)
        except:
            pass
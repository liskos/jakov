for p in range(30,36):
    for s in range(12,34):
        x1 = int("R4",p-1)
        x2 = int("B0",s+2)
        x3 = int("T3NK4",p)
        if x1+x2+x3 == 23593399:
            print(p,s,p*s)
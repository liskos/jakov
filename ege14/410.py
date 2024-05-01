for p in range(2,100):
    for q in range(2,100):
        s1 = 10 * p ** 2 + 11 * p ** 1 + 12
        s2 = 11 * q ** 2 + 12 * q ** 1 + 13
        if s1 == s2:
            print(p,q,s1)
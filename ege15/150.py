for a in range(1, 1000):
    if all(((x & 56) == 0) or ((x & 48) != 0) or ((x & a) != 0) for x in range(1, 1000)):
        print(a)
        break

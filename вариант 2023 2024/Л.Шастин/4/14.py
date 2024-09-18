for x in "01234":
    for y in "01234":
        s = 5 ** 50 + 5 ** 30 - 5 ** x - y - 5 ** y - x
        if s.count("0")==10:
            print(x*y)
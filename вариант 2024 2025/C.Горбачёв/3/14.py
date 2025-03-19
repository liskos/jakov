for x in range(1,3053):
    s = 4 ** 151 + 7 ** 283 + 6 ** 82 - 5 * x
    s = oct(s)[2:]
    if s.count("1") == 26:
        print(x)

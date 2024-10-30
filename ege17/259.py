a = [int(x) for x in open("17data/17-257.txt")]
b11 = [x for x in a if x % 11 == 0]
b17 = [x for x in a if x % 17 == 0]


if max(b11) > max(b17):
    print(len(b11),min(b11))
else:
    print(len(b17), max(b17))
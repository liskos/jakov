import itertools
b = set()
for a in itertools.permutations("РЕЖИМДНО",r=6):
    ss = "".join(a).replace("Р","Н").replace("Ж","Н").replace("М","Н").replace("Д","Н")
    ss = "".join(a).replace("Е","О").replace("И","О")
    if ss[0] == "Н" and ss[1] == "О" and ss[1] == "О":
        b.add(a)


print(len(b),b)
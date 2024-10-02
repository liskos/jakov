import itertools
b = set()
for a in (itertools.permutations("КОМПЬЮТЕР",r=9)):
    ss = "".join(a).replace("Е","1").replace("К","2").replace("М","3").replace("О","4").replace("П","5").replace("Р","6").replace("Т","7").replace("Ь","8").replace("Ю","9")
    if a[-2] == "Е" and int(ss[0]) < int(ss[1]) < int(ss[2]) < int(ss[3]):
        b.add(a)
print(len(b),b)

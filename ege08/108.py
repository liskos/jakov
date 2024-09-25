import itertools
b = set()
for a in (itertools.permutations("КОМЕТА",r=6)):
    ss = "".join(a).replace("К","Т").replace("О","А").replace("М","Т").replace("Е","А")
    if ("ТТ" not in ss)and("АА" not in ss):
        b.add("".join(a))
print(len(b),b)


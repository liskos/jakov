import itertools
b = set()
for a in itertools.permutations("АВТОМАТ",r=7):
    ss = "".join(a).replace("В","Т").replace("М","Т")
    ss = ss.replace("О","А")
    if ("АА" not in ss) and ("ТТ" not in ss):
        b.add(a)

print(len(b))
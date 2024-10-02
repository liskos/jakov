import itertools
b = set()
for a in itertools.permutations("АВТОРОТА",r=8):
    ss = "".join(a).replace("А","О")
    ss = ss.replace("В","Т").replace("Р","Т")
    if "ОО" not in ss and "ТТ" not in ss:
        b.add(a)

print(len(b))
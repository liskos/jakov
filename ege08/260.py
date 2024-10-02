import itertools
b = set()
for a in itertools.permutations("ТИХОРЕЦК",r=4):
    ss = "".join(a).replace("И","Е").replace("О","Е")
    if ss.count("Е") == 2 and ((a[0] == "Т" and a[1] == "И") or (a[0] == "Т" and a[3] == "О") or (a[0] == "Т" and a[2] == "Х") or (a[1] == "И" and a[3] == "О") or (a[1] == "И" and a[3] == "О") or (a[1] == "И" and a[2] == "Х") or (a[3] == "О" and a[2] == "Х")):
        b.add(a)

print(len(b))
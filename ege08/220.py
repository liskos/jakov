import itertools
b = set()
for a in itertools.permutations("СОТКАПЛЗ",r=5):
    ss = "".join(a).replace("О","А")
    if ss[-1] != "А" and "ЗЛО" not in "".join(a):
        b.add(a)

print(len(b),b)
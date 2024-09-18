import itertools
b = set()
for a in itertools.permutations("ТАРКНИЩЕ",r = 6):
    s =  ''.join(a)
    ss = s.replace("Р","Т").replace("К","Т").replace("Н","Т").replace("Щ","Т")
    ss = ss.replace("И","А").replace("Е","А")
    if ss[0] == "Т" and ("ТТ" not in ss) and ("АА" not in ss):
        b.add(a)
print(len(b))

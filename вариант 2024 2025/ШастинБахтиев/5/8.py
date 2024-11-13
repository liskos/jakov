import itertools
k = 0
for a in itertools.product("АВИЙКПС",repeat=6):
    ss = "".join(a).replace("И","А")
    if ss.count("АА") > 0:
        k += 1

        if "".join(a) == "КАКААА":
            print(k,a)
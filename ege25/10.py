def delitel(n):
    a = set()
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    return sorted(a)


for n in range(338472,338494+1):
    divs = delitel(n)
    if len(divs) == 4:
        print(* divs)


# 1 271 1249 338479
# 1 2 169241 338482
# 1 59 5737 338483
# 1 2 169243 338486
# 1 23 14717 338491
# 1 3 112831 338493

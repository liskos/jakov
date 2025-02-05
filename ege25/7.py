def delitel(n):
    a = set()
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    return sorted(a)


for n in range(113012,113061+1):
    divs = delitel(n)
    if len(divs) == 4:
        print(* divs)


#1 2 56509 113018
# 1 2 56519 113038
# 1 131 863 113053
# 1 2 56527 113054
# 1 167 677 113059
for n in range(102714,102725+1):
    div = [d for d in range(1,n+1) if n % d == 0]
    if len(div) == 4:
        print(* div)


def delitel(n):
    a = set()
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    return sorted(a)

for n in range(102714,102725+1):
    divs = delitel(n)
    if len(divs) == 4:
        print(*divs)


# 1 5 20543 102715
# 1 59 1741 102719
# 1 139 739 102721
# 1 2 51361 102722
def delitel(n):
    a = set()
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    return sorted(a)


for n in range(222987,223022):
    divs = delitel(n)
    if len(divs) == 4:
        print(* divs)

# 1 2 111497 222994
# 1 173 1289 222997
# 1 269 829 223001
# 1 7 31859 223013
# 1 2 111509 223018
# 1 83 2687 223021
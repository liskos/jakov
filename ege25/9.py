def delitel(n):
    a = set()
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    return sorted(a)


for n in range(258274,258297+1):
    divs = delitel(n)
    if len(divs) == 4:
        print(* divs)

# 1 17 15193 258281
# 1 181 1427 258287
# 1 173 1493 258289
# 1 7 36899 258293
# 1 5 51659 258295
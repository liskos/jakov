def delitel(n):
    a = set()
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    return sorted(a)


for n in range(251811,251827):
    divs = delitel(n)
    if len(divs) == 4:
        print(*divs)


#1 31 8123 251813
# 1 5 50363 251815
# 1 3 83939 251817
# 1 419 601 251819
# 1 17 14813 251821
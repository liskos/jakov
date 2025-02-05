def delitel(n):
    a = set()
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    return sorted(a)

for n in range(118811,118972+1):
    divs = delitel(n)
    if len(divs) == 6:
        print(*divs)

# 1 2 4 29717 59434 118868
# 1 2 4 29723 59446 118892
# 1 11 121 983 10813 118943
# 1 3 9 13217 39651 118953
# 1 2 4 29741 59482 118964
# 1 3 9 13219 39657 118971
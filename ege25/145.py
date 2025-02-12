def proverk(n):
    for b in str(n):
        if int(b) > 2:
            return False

    if sum(map(int,str(n))) % 10 == 0:
        return True
    else:
        return False

def delitel(n):
    a = set()
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    return a


a = []
for n in range(1000000,1300000+1):
    if proverk(n):
        a.append(n)
for i in a[9::10]:
    print(i, len(delitel(i)))
# 1000220 22
# 1002000 78
# 1010010 30
# 1011020 10
# 1012100 34
# 1020110 62
# 1021120 26
# 1022200 46
# 1100210 14
# 1101220 10
# 1110000 98
# 1111010 14
# 1112020 70
# 1120100 34
# 1121110 6
# 1122120 62
# 1200200 46
# 1201210 6
# 1202220 34
# 1211000 62
# 1212010 14
# 1220020 10
# 1221100 16
# 1222110 46
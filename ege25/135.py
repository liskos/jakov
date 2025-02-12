def delitel(n):
    a = set()
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    chet = [x for x in a if x % 2 == 0]
    chet.append(1)
    if len(chet) == 1 and len(a) > 70:
        return True,max(a)
    else:
        return False






for i in range(321654,654321+1):
    if delitel(i):
        print(i,delitel(i)[1])

#405405 135135
# 530145 176715
# 592515 197505
# 626535 208845
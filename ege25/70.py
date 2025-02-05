def delitel(n):
    a = set()
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    a.add(1)
    return sum(a),len(sorted(a))


b = []

for n in range(2,10000+1):
    if n == delitel(n)[0]:
        print(n,delitel(n)[1])

#6 4
# 28 6
# 496 10
# 8128 14
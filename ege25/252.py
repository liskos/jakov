
def delitel(n):
    u = 1
    a = set()
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    for x in a:
        u *= x
    return a,u

for i in range(1000000,1900000):
    if sum(delitel(i)[0]) % 2 != 0 and delitel(i)[1] % 2 != 0 and len(delitel(i)[0]) > 40:
        print(i,len(delitel(i)[0]))


# 1071225 45
# 1147041 45
# 1334025 81
# 1432809 45
# 1625625 45
# 1656369 45
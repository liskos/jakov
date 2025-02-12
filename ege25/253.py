
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

for i in range(2000000,3000000):
    if sum(delitel(i)[0]) % 2 != 0 and delitel(i)[1] % 2 != 0 and len(delitel(i)[0]) > 30:
        print(i,len(delitel(i)[0]))



# 2030625 45
# 2099601 45
# 2205225 63
# 2480625 75
# 2614689 45
# 2772225 45

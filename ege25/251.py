
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

for i in range(800001,1500000):
    if sum(delitel(i)[0]) % 2 != 0 and delitel(i)[1] % 2 != 0 and len(delitel(i)[0]) > 10:
        print(i,len(delitel(i)[0]))

# 804609 27
# 815409 27
# 826281 15
# 837225 27
# 855625 15
# 859329 15
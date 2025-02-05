def delitel(n):
    a = set()
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    return a

for n in range(1000,20000+1):
    divs = delitel(n)
    if n - (sum(divs) - n) == 1:
        print(n)

# 1024
# 2048
# 4096
# 8192
# 16384
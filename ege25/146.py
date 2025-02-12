def prost(n):
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
def delitel(n):
    a = set()
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    chet = [x for x in a if x % 2 == 0]

    return sorted(a)[1]


for n in range(7072,7107):
    if prost(n):
        print(n**2*2,delitel(n**2*2))
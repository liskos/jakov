def sum_del(n):
    a = set()
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)

    return sum(a)

for i in range(2,263000+1):
    d = sum_del(i)
    if i * 2 == sum_del(d):
        print(i)
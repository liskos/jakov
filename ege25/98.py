def delitel(n):
    a = set()
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    return a


for n in range(228224,531135+1):
    divs = delitel(n)
    if (sum(divs)-n-1) > 460000:
        print(len(divs),sum(divs))


# 144 624960
# 120 619008
# 128 622080
# 120 620730
# 120 638352
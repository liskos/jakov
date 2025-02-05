def delitel(n):
    a = set()
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    return sorted(a,reverse=True)

for n in range(190201,190230+1):
    divs = delitel(n)
    if len(divs) == 4:
        print(*divs)

# 190201 17291 11 1
# 190202 95101 2 1
# 190214 95107 2 1
# 190219 853 223 1
# 190222 95111 2 1
# 190223 17293 11 1
# 190227 63409 3 1
# 190229 14633 13 1
import fnmatch
def delitel(n):
    a = set()
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    x = [x for x in a if x % 2 == 0]
    return x


for n in range(65001,10000000):
    if fnmatch.fnmatch(str(n),"6*97*5?"):
        if len(delitel(n)) > 3:
            print(n,sum(delitel(n)))


# 69750 129792
# # 69752 122080
# # 69756 139536
# # 69758 75152
# # 609750 1103232
# # 609752 1291248
# # 609754 630840
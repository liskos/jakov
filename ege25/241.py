import fnmatch
def delitel(n):
    a = set()
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    return a
for i in range(1,1000000):
    if fnmatch.fnmatch(str(i),"?6*6*?6"):
        if i % 6 == 0 and i % 7 == 0 and i % 8 == 0:
            print(i,sum(delitel(i)))


#
# 56616 162240
# 66696 191040
# 161616 527744
# 166656 523264
# 266616 862680
# 360696 1094400
# 366576 1083264

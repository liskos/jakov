import fnmatch

for i in range(51,10**6+1,51):
    if fnmatch.fnmatch(str(i),"12*45*"):
        print(i,i//51)


# 122145 2395
# 122451 2401
# 124542 2442
# 124593 2443
# 127245 2495
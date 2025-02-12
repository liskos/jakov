import fnmatch


for i in range(2023,10**9+1,2023):
    if fnmatch.fnmatch(str(i),"20*23"):
        if 20 > sum(map(int,str(i))) and sum(map(int,str(i))) % 7 == 0:
            print(i,i//2023)


# 2023 1
# 204323 101
# 2025023 1001
# 20232023 10001
# 202302023 100001
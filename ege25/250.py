import fnmatch

for i in range(1,10**11+1):
    if fnmatch.fnmatch(str(i),"12345*76") and i % 73 == 0:
        print(i,i//73)





# 1234576 16912
# 12345176 169112
# 123451176 1691112
# 123458476 1691212
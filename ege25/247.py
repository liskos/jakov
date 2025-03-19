import fnmatch

for i in range(700000,1000000):
    if fnmatch.fnmatch(str(i),"*0??3*")==False and fnmatch.fnmatch(str(i),"*4??2")==False and fnmatch.fnmatch(str(i),"*1*") == False:
        if i % 13 == 0:
            print(i,sum(map(int,str(i))))



# 700024 13
# 700050 12
# 700076 20
# 700089 24
# 700206 ege15
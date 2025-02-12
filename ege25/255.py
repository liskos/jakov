import fnmatch

for i in range(9797,10**7+1,9797):
    if fnmatch.fnmatch(str(i),"3Р1"):
        print(i,i//9797)
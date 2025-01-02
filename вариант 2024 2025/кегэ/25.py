import fnmatch

for i in range(18579,10**10+1,18579):
    if fnmatch.fnmatch(str(i),"54?1?3*7"):
        print(i,i//18579)
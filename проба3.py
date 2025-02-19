import fnmatch
for i in range(2024,10**10+1,2024):
    if fnmatch.fnmatch(str(i),"1*2322?2"):
        print(i,i//2024)
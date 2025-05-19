import fnmatch

for i in range(50825,10**13+1,50825):
    if fnmatch.fnmatch(str(i),"21?78914?*25"):
        print(i,i//50825)
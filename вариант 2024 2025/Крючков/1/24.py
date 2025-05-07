s = open("24(2).txt").read()
import time
t1 = time.time()
l = 0
r = 0
m = 0
for i in range(1,len(s)):
    if s[i-1] <= s[i]:
        r = i
        m = max(m, r - l + 1)
    else:
        l = i
print(m)
print(time.time() - t1)
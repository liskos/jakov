s = open("24data/24-1.txt").read()

t = 0
m = 0
k = 0
for i in range(1,len(s)-1):
    if s[i] < s[i-1] and s[i] < s[i+1]:
        k = i - t
        m = max(m,k)

        t = i

print(m)
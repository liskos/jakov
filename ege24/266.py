s = open("24data/24-263.txt").readline()
k = 0
l = 0
m = 100000000

for i in range(len(s)):
    if s[i] == "Z":
        k += 1
        while k >= 120:
            if s[l] == "Z":
                k -= 1
            l += 1
            if k == 120:
                m = min(m,i-l+1)

print(m)
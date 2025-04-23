s = open("24data/24-263.txt").readline()
k = 0
l = 0
m = 100000000
t = ""
for i in range(len(s)):
    if s[i] == "Z":
        k += 1
        while True:
            if k <= 120 and s[l] == "Z":
                break
            if s[l] == "Z":
                k -= 1
            l += 1
    if k >= 120:
        if i-l+1 < m:
            m = i-l+1
            t = s[l:i+1]


print(m, t)
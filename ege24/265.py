s = open("24data/24-263.txt").read()
k = 0
m = 0
l = 0

for i in range(len(s)):
    if s[i] == "Y":
        k += 1
        while k > 150:
            if s[i] == "Y":
                k -= 1
            l += 1
    m = max(m,i-l+1)

print(m)
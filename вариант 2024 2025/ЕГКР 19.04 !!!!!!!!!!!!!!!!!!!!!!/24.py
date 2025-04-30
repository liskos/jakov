s = open("24_21717.txt").read()

m = 100000
l = 0
k = 0
t = ""
for i in range(len(s)):
    if s[i:i+3] == "RSQ":
        k += 1
        while k > 130:
            if s[l:l+3] == "RSQ":
                k -=1
            l += 1
    if k == 130:
        m = min(m,i-l+1)

print(m)
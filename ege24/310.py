s = open('24data/24_13715__3kjzr.txt').read()
k = 0
m = 0
l = 0
for i in range(len(s)):
    if s[i:i+2] == "CD":
        k += 1
        while k > 50:
            if s[l:l+2] == "CD":
                k -= 1
            l += 1
    if k == 50:
        m = max(m,i-l+2)


print(m)

s = open('24data/24_13715__3kjzr.txt').readline().replace('CD', 'C_D').split('_')
mx = 0
for i in range(len(s)-50):
    word = ''.join(s[i:i+51])
    mx = max(mx,len(word))
print(mx)

#екстовый файл состоит из символов A, B, C, D и E. Определите в прилагаемом файле максимальное количество идущих подряд символов, среди которых комбинация символов CD встречается ровно 50 раз.
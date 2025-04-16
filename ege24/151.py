s = open("24data/24-j9.txt").read()
b = ""
k = 0
for i in range(len(s)-4):
    b = s[i:i+5]
    if b == b[::-1]:  # проверка на палиндром
        k += 1

print(k)
s = open("24data/24.txt").read()

t = ""
maxlen = 0
maxstroka = ""
index_prime_sumvola = 0

for i in range(len(s)):
    if t == "": # если нет текущей строки, то начинаем новую
        t = s[i]
    elif t[-1] <= s[i]:
        t += s[i] # если текущий элемент больше последнего элемента текущей строки, то добавляем его в конец строки
    else:
        t = s[i] # если текущий элемент меньше последнего элемента текущей строки,то начинаем новую строку с текущим элементом

    if len(t) > maxlen:
        maxlen = len(t)
        maxstroka = t
        index_prime_sumvola = i - len(t) + 1

print(maxlen)
print(maxstroka)
print(index_prime_sumvola)

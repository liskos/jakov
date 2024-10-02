import itertools

b = set()
d = 26655

for i, a in enumerate(itertools.product("АИКЛМЬ", repeat=6), 1):
    if a[0] == "К" and a[-1] == "Ь" and len(set(a)) == 6:
        b.add(a)
        print(i)
        if abs(i - int(''.join(reversed(str(i))))) == d:
            print(f"Найдено слово: {''.join(a)}, номер: {i}")
            sum_of_digits = sum(int(digit) for digit in str(i))
            print(f"Сумма цифр номера: {sum_of_digits}")
            break

print(len(b), b)
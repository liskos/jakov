a = [int(x) for x in open("17data/17-367.txt")]

max_length = 0
max_sum = 0
current_length = 1
current_sum = a[0]

for i in range(1, len(a)):
    if a[i] % a[i-1] == 0 or a[i-1] % a[i] == 0:
        current_length += 1
        current_sum += a[i]
    else:
        if current_length > max_length:
            max_length = current_length
            max_sum = current_sum
        current_length = 1
        current_sum = a[i]

# Проверка последней цепочки
if current_length > max_length:
    max_length = current_length
    max_sum = current_sum

print(max_length, max_sum)
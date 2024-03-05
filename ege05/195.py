def f(n):
    b = bin(n)[2:]
    while b != 0:
        sum_of_digits = sum(int(digit) for digit in b)
        b = b + str(sum_of_digits % 2)
        if int(b,2 >= 50):
            break
    while b != 0:
        sum_of_digits = sum(int(digit) for digit in b)
        b = b + str(sum_of_digits)
        if int(b,2 >= 50):
            break
    return int(b,2)


print(f(13))
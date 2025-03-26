
for a in range(1, 300):
    if all([(not(x <= 9) or (x * x <= a)) and (not(y * y <= a) or (y <= 10)) for x in range(1, 300) for y in range(1, 300)]):
        print(a)

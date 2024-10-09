def f(n):
    b = bin(n)[2:]
    if b.count("0") > b.count("1"):
        b = b.replace("0","8")
        b = b.replace("1","0")
        b = b.replace("8","1")
        return int(b, 2)
    else:
        modified_binary = ''
        for index in range(len(b)):
            if index % 2 == 0:  # Четная позиция
                modified_binary += '1'
            else:
                modified_binary += b[index]
        return int(modified_binary,2)

for i in range(2,10000):
    if f(i) < 1338:
        print(i)
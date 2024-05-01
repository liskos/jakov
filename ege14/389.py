for x in "123456789":
    s1 = 1 * int(f"3{x}51") ** 2 + 2 * int(f"3{x}51") + 3
    s2 = 1 * int(f"1{x}3") ** 2 + int(x,15) * int(f"1{x}3") + 3
    s3 = 1 * (int(x,15)+1)**2 + int(x,15)*(int(x,15)+1) + 2
    s = int(f"3{x}15{x}",15) + s1 + int(x,15) ** int(x,15) + s2 + s3
    if s % 13 == 0:
        print(s)
        break
r = '0123456789abc'
b = ""
while s>0:
    b = r[s%13] + b
    s //= 13
print(b)



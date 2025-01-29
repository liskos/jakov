# def d(n):
#     s = ""
#     t = "012345678"
#     while n > 0:
#         s = t[n%9] + s
#         n //= 9
#     return s
#
# def f(n):
#     b = d(n)
#     if sum(map(int,b)) % 2 == 0:
#         b += "52"
#     else:
#         b = "73" + b[2:] + "44"
#     return int(b,9)
#
#
# for i in range(1,100000):
#     if f(i) > 13950:
#         print(i)

#12 200   8281  1976
print(444+364-182  )
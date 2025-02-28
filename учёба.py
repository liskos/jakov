# x = 15 + 20 + \
#     30
# print(x)
#
# s = input()
# s = sorted(s,key=lambda x: -( x == 0))
# print(s)
#


for x in range(37):
    s1 = 9 * 37 ** 4 + 8 * 37 ** 3 + x * 37 ** 2 + 3 * 37 ** 1 + 1
    s2 = 1 * 37 ** 4 + x * 37 ** 3 + 9 * 37 ** 2 + 2 * 37 ** 1 + 4
    if (s1 + s2) % 21 == 0:
        print(x,(s1+s2)/21)
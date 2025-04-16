import string
def d(n):
    t = "0123456789abcdefghijklm"
    s = ""
    while n > 0:
        s = t[n%23] + s
        n //= 23
    return s

k = 0
s = 9 * 123 ** 2053 + 5 * 23 ** 3146 + 91 * 47 ** 5533 + 4099
s = d(s)
for i in range(len(s)):
    if int(s[i],23) > 15:
        k += 1

print(k)
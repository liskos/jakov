def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)

def tr(n):
    t = "012"
    s = ""
    while n > 0:
        s = t[n%3] + s
        n //= 3
    return s

a = [int(x) for x in open("17data/17-4.txt")]
r = []
for i in range(len(a)):
    if ((sum_of_digits(a[i])) % 5 == 0) and (tr(abs(a[i]))[-2:] != "00"):
        r.append(a[i])
print(len(r),max(r))
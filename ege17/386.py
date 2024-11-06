a = [int(x) for x in open("17data/17-386.txt")]
r = []
b = []
def f(x,y,z):
    return str(x).count("3") == 1 and str(y).count("3") == 1 and str(z).count("3") == 1

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

for i in range(len(a)-2):
    if f(a[i],a[i+1],a[i+2]) and is_prime(a[i]+a[i+1]+a[i+2]):
        r.append(a[i]+a[i+1]+a[i+2])

print(len(r),min(r))
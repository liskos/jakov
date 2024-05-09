def f(s):
    while '23' in s:
        s = s.replace('23', '7', 1)
    return s

for n in range(1, 11):
    s = "23" * n + (10 - n) * "3"
    print(n, sum(map(int,f(s))))
for n in range(11, 25):
    s = "23" * 10 + (n-10) * "2"
    print(n, sum(map(int,f(s))))
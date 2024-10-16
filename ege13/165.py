import ipaddress
a = set()
def ch(n):
    t = "0123"
    s = ""
    while n > 0:
        s = t[n%4]+ s
        n //= 4
    return s
net = ipaddress.IPv4Network("192.168.0.0/17",0)
for ip in net:
    if int(ip) % 4 == 0:
        a.add(ip)
print(len(a))
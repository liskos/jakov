
import ipaddress
for m in range(0,256):
    net = ipaddress.ip_network(f"192.214.{m}.184/255.255.255.224",0)
    d = 0
    k = 0
    for ip in net:
        k += 1
        if ip.__format__("b").count("1") > 15:
            d += 1
    if d == k:print(m)

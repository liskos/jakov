
import ipaddress
for m in range(1,32):
    net = ipaddress.ip_network(f"250.113.{m}.197/255.255.255.192",0)
    if all(ip.__format__("b")[:16].count("1") >= ip.__format__("1")[16:].count("0") for ip in net):
        print(net.netmask)

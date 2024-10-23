
import ipaddress
for m in range(0,255):
    net = ipaddress.ip_network(f"227.31.{m}.139/255.255.255.224",0)
    if all(ip.__format__("b")[:16].count("0") <= ip.__format__("b")[16:].count("0") for ip in net):
        print(net,m)

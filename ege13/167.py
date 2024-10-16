import ipaddress
net = ipaddress.ip_network("140.19.96.0/255.255.248.0",0)
b = set()
for ip in net:
    if (ip.packed[0].__format__("b").count("1") == ip.packed[1].__format__("b").count("1") ==
         ip.packed[2].__format__("b").count("1") == ip.packed[3].__format__("b").count("1")):
        b.add(ip)

print(len(b))
import ipaddress
k = 0
net = ipaddress.ip_network("140.116.194.0/255.255.240.0",0)
for ip in net:
    if ((ip.packed[0].__format__("b")[-1] == "0") and (ip.__format__("b")[15] == "0") and (ip.__format__("b")[23] == "0") and (ip.__format__("b")[31] == "0")):

        k += 1
print(k)
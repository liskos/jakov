import ipaddress
k = 0
net = ipaddress.ip_network("140.116.194.0/255.255.240.0",0)
for ip in net:
    if ((ip.__format__("b")[3] == "0") and (ip.__format__("b")[7] == "0") and (ip.__format__("b")[12] == "0") and (ip.__format__("b")[15] == "0")):
        k += 1
print(k)
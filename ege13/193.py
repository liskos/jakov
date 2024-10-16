import ipaddress
net = ipaddress.ip_network("154.24.165.32/255.255.255.224",0)

for ip in net:
     if ip.__format__("b")[0:14].count("1") > ip.__format__("b")[15:31].count("1"):
         print(ip)

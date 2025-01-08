import ipaddress
net = ipaddress.ip_network("218.194.82.148/255.255.255.192",0)

for ip in net:
    print(ip)